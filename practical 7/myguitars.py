# My guitar

from guitars import Guitar
import csv


def main():
    guitars = read_guitars_from_file("guitars.csv")
    display_guitars(guitars)
    add_new_guitars(guitars)
    write_guitars_to_file("guitars.csv", guitars)

    guitars.sort()
    print("\nGuitars sorted by year:")
    display_guitars(guitars)


def read_guitars_from_file(filename):
    guitars = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)
    return guitars


def display_guitars(guitars):
    print("These are my guitars:")
    for guitar in guitars:
        print(guitar)


def add_new_guitars(guitars):
    print("\nAdd new guitars:")
    while True:
        name = input("Name: ")
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)


def write_guitars_to_file(filename, guitars):
    with open(filename, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


if __name__ == "__main__":
    main()
