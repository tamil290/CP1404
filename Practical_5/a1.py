

VISITED = 'v'
UNVISITED = 'n'


def main():
    """Main Function"""

    print("Travel Tracker 1.0 - by <TAMILSELVAN ANBALAGAN>")
    print("3 places loaded from places.csv")

    temp_data = []

    read_file = open("places.csv", "r")  # read csv file
    new_data = add_places_into_new_array(read_file)
    read_file.close()

    for data in new_data:  # add read file data to temp memory list

        temp_data.append(data)

    display_menu()
    user = input(">>> ")

    while user == "":  # user input is empty

        print("Input can not be blank")

        user = input(">>> ")

    while user != "":

        if user.upper() == "L":

            display_places(temp_data)
            display_menu()
            user = input(">>> ")

        elif user.upper() == "A":

            add_place(temp_data)
            display_menu()
            user = input(">>> ")

        elif user.upper() == 'R':

            recommend_place(temp_data)
            display_menu()
            user = input(">>> ")

        elif user.upper() == "M":

            place_visited(temp_data)
            display_menu()
            user = input(">>> ")

        elif user.upper() == "Q":

            save_and_quit(temp_data)
            break
        else:

            print("Invalid menu choice")
            display_menu()
            user = input(">>> ")

    return user


def display_menu():
    """Display Menu"""

    print("\nMenu")
    print("L - List places")
    print("R - Recommend place")
    print("A - Add new place")
    print("M - Mark a place as visited")
    print("Q - Quit")


def add_places_into_new_array(read_file):
    """List of places"""

    new_data = []

    for line in read_file:
        line = line.strip()  # Remove \n
        parts = line.split(',')  # Separate data
        parts[2] = int(parts[2])  # Convert integer
        new_data.append(parts)

    return new_data


def display_places(places):
    places.sort(key=lambda p: (p['visited'], p['priority'], p['name']))
    visited_count = 0
    unvisited_count = 0
    for i, place in enumerate(places, 1):
        mark = '*' if place['visited'] == UNVISITED else ' '
        print(f"{mark}{i}. {place['name']} in {place['country']} priority {place['priority']}")
        if place['visited'] == VISITED:
            visited_count += 1
        else:
            unvisited_count += 1
    print(f"{len(places)} places. You still want to visit {unvisited_count} places.")
    if visited_count == len(places):
        print("No places left to visit. Why not add a new place?")


def add_place(places):
    name = input("Name: ")
    while not name:
        print("Input can not be blank")
        name = input("Name: ")
    country = input("Country: ")
    while not country:
        print("Input can not be blank")
        country = input("Country: ")
    priority = input("Priority: ")
    while not priority.isdigit():
        print("Invalid input; enter a valid number")
        priority = input("Priority: ")
    priority = int(priority)
    places.append({'name': name, 'country': country, 'priority': priority, 'visited': UNVISITED})


def recommend_place(places):
    unvisited_places = [place for place in places if place['visited'] == UNVISITED]
    if not unvisited_places:
        print("No places left to visit!")
        return
    random_place = random.choice(unvisited_places)
    print(f"Not sure where to visit next? How about... {random_place['name']} in {random_place['country']}?")


def place_visited(temp_data):
    """Mark unvisited place to visited"""

    count = 0

    for unvisited in temp_data:  # counting unvisited place

        if unvisited[3] == "n":
            count += 1

    if count != 0:

        while True:

            display_places(temp_data)

            try:

                mark_place = int(input("Enter the number of a place to mark as visited \n>>>"))

                while mark_place <= 0:
                    print("Place number must be greater than 0")

                    mark_place = int(input("Enter the number of a place to mark as visited \n>>>"))

                while mark_place > len(temp_data):
                    print("No place number found !")

                    mark_place = int(input("Enter the number of a place to mark as visited \n>>>"))

                while len(temp_data) >= mark_place > 0:

                    for i, data in enumerate(temp_data):

                        i += 1

                        if i == mark_place:

                            if data[3] == "n":

                                data[3] = "v"
                                print(data[0], "in", data[1], "is visited")

                            else:

                                print("Place is already visited")

                            return temp_data

                return mark_place

            except ValueError:

                print("\nPlease, Enter place number only !!\n")
    else:

        print("No unvisited places")


def save_and_quit(temp_data):
    """Save all the places into csv file and stop the program"""

    output_file = open("places.csv", "w", newline="")

    for data in temp_data:
        data[2] = str(data[2])  # Convert into string
        write = ','.join(data)
        print(write, file=output_file)  # write data into csv

    output_file.close()

    print(len(temp_data), "places saved to places.csv")
    print("Have a nice day : )")


main()

print("")

print("Created By Min Khant Soe (HakHak)")

input("")
