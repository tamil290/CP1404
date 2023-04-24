import csv
import random

VISITED = 'v'
UNVISITED = 'n'

MENU_OPTIONS = {
    'L': 'List places',
    'R': 'Recommend random place',
    'A': 'Add new place',
    'M': 'Mark a place as visited',
    'Q': 'Quit'
}


def main():
    """The main function that runs the Travel Tracker program."""

    print("Travel Tracker 1.0 - by <TAMILSELVAN ANBALAGAN>")
    places = load_places()
    display_menu()
    choice = get_menu_choice()

    while choice != 'Q':
        if choice == 'L':
            display_places(places)
        elif choice == 'R':
            recommend_place(places)
        elif choice == 'A':
            add_place(places)
        elif choice == 'M':
            place_visited(places)
        else:
            print("Invalid menu choice")

        display_menu()
        choice = get_menu_choice()

    save_and_quit(places)
    print("Have a nice day : )")


def display_menu():
    """Display the menu options for the user to select."""

    print("\nMenu")
    for option, description in MENU_OPTIONS.items():
        print(f"{option} - {description}")


def get_menu_choice():
    """Get the user's choice of menu option."""

    while True:
        choice = input(">>> ").upper()
        if choice in MENU_OPTIONS:
            return choice
        print("Invalid menu choice")


def load_places():
    """Load the places from the places.csv file and return them as a list of dictionaries."""

    places = []
    try:
        with open("places.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                name, country, priority, visited = row
                places.append({'name': name, 'country': country, 'priority': int(priority), 'visited': visited})
        print(f"{len(places)} places loaded from places.csv")
    except FileNotFoundError:
        print("places.csv not found")
    return places


def display_places(places):
    """Display the places in the order of visited status, priority, and name."""

    places.sort(key=lambda p: (p['visited'], p['priority'], p['name']))
    visited_count = 0
    unvisited_count = 0
    for i in range(len(places)):
        place = places[i]
        mark = '*' if place['visited'] == UNVISITED else ' '
        print(f"{mark}{i + 1}. {place['name']} in {place['country']} priority {place['priority']}")
        if place['visited'] == VISITED:
            visited_count += 1
        else:
            unvisited_count += 1
    print(f"{len(places)} places. You still want to visit {unvisited_count} places.")
    if visited_count == len(places):
        print("No places left to visit. Why not add a new place?")


def recommend_place(places):
    """Recommend a random unvisited place to visit."""

    unvisited_places = [place for place in places if place['visited'] == UNVISITED]
    if not unvisited_places:
        print("No places left to visit!")
        return
    random_place = random.choice(unvisited_places)
    print(f"Not sure where to visit next? How about... {random_place['name']} in {random_place['country']}?")


def add_place(places):
    name = input("Name: ")
    while not name:
        print("Name input cannot be blank")
        name = input("Name: ")
    country = input("Country: ")
    while not country:
        print("Country input cannot be blank")
        country = input("Country: ")
    priority = input("Priority: ")
    while not priority.isdigit():
        print("Invalid input; enter a valid number")
        priority = input("Priority: ")
    priority = int(priority)
    places.append({'name': name, 'country': country, 'priority': priority, 'visited': UNVISITED})
    print(f"{name} in {country} (priority {priority}) has been added to the Travel Tracker.")


def place_visited(places):
    """Mark unvisited place as visited"""

    unvisited_count = sum(1 for place in places if place['visited'] == UNVISITED)

    if unvisited_count != 0:
        while True:
            display_places(places)

            try:
                mark_place = int(input("Enter the number of a place to mark as visited\n>>>"))

                while mark_place <= 0 or mark_place > len(places):
                    if mark_place > 0:
                        print("Invalid place number")
                    else:
                        print("Number must be > 0")
                    mark_place = int(input("Enter the number of a place to mark as visited\n>>>"))

                place = places[mark_place - 1]

                if place['visited'] == UNVISITED:
                    place['visited'] = VISITED
                    print(f"{place['name']} in {place['country']} visited!")
                else:
                    print(f"You have already visited {place['name']}.")

                return places

            except ValueError:
                print("Invalid input; enter a valid number.")

    else:
        print("No unvisited places.")


def save_and_quit(places):
    """Save all the places into csv file and stop the program"""

    with open("places.csv", "w", newline="") as output_file:
        writer = csv.writer(output_file)

        for place in places:
            place_data = [place['name'], place['country'], str(place['priority']), place['visited']]
            writer.writerow(place_data)

    print(len(places), "places saved to places.csv")


main()

print("")

input("")
