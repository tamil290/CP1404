from project import Project
import os
from datetime import datetime


def main():
    projects = load_projects("projects.txt")

    while True:
        print("\n- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")

        choice = input(">>> ").lower()
        if choice == 'l':
            filename = input("Enter a filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Enter a filename to save projects to: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            date_input = input("Show projects that start after date (dd/mm/yy): ")
            filter_date = datetime.strptime(date_input, "%d/%m/%Y").date()
            filtered_projects = [project for project in projects if project.start > filter_date]
            for project in filtered_projects:
                print(project)
        elif choice == 'a':
            name = input("Project name: ")
            start = input("Start date (dd/mm/yyyy): ")
            priority = input("Priority: ")
            estimate = input("Cost estimate: ").replace(',', '').replace('$', '')
            completion = input("Completion percentage: ")
            new_project = Project(name, start, priority, estimate, completion)
            projects.append(new_project)
        elif choice == 'u':
            for i, project in enumerate(projects):
                print(f"{i} {project}")
            project_index = int(input("Project choice: "))
            chosen_project = projects[project_index]
            print(chosen_project)
            new_percentage = input("New Percentage: ")
            new_priority = input("New Priority: ")
            if new_percentage:
                chosen_project.completion = int(new_percentage)
            if new_priority:
                chosen_project.priority = int(new_priority)
            pass
        elif choice == 'q':
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice. Please try again.")


def load_projects(filename):
    projects = []
    with open(filename, "r") as file:
        file.readline()  # Skip header line
        for line in file:
            fields = line.strip().split("\t")
            projects.append(Project(*fields))
    return projects


def save_projects(filename, projects):
    with open(filename, "w") as file:
        file.write("Name\tStart\tPriority\tEstimate\tCompletion\n")
        for project in projects:
            file.write(
                f"{project.name}\t{project.start.strftime('%d/%m/%Y')}\t{project.priority}\t{project.estimate}\t{project.completion}\n")


def display_projects(projects):
    incomplete_projects = sorted([project for project in projects if project.completion < 100],
                                 key=lambda p: int(p.priority))
    completed_projects = sorted([project for project in projects if project.completion == 100],
                                key=lambda p: int(p.priority))

    print("Incomplete projects:")
    for project in incomplete_projects:
        print("  ", project)

    print("Completed projects:")
    for project in completed_projects:
        print("  ", project)


main()
