# Game, Set, Match


import csv


def main():
    # Read the CSV file
    data = read_csv_file("wimbledon.csv")

    # Get the champions and the number of times they have won
    champions = get_champions(data)

    # Display the champions and the number of times they have won
    print("Wimbledon Champions:")
    for name, count in champions.items():
        print(f"{name} {count}")

    # Get the countries of the champions
    countries = get_countries(data)

    # Display the countries of the champions in alphabetical order
    print("\nThese", len(countries), "countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def read_csv_file(filename):
    """
    Reads a CSV file and returns its contents as a list of lists.
    """
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        return [row for row in reader]


def get_champions(data):
    """
    Returns a dictionary containing the champions and the number of times they have won.
    """
    champions = {}
    for row in data:
        if row[0] != "Year":  # Skip the header row
            name = row[2]
            champions[name] = champions.get(name, 0) + 1
    return champions


def get_countries(data):
    """
    Returns a set of the countries of the champions.
    """
    countries = set()
    for row in data:
        if row[0] != "Year":  # Skip the header row
            country = row[1]
            countries.add(country)
    return countries


main()
