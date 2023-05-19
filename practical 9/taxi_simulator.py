# Taxi Simulator

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_bill = 0.0
    current_taxi = None

    print("Let's drive!")
    while True:
        print("q)uit, c)hoose taxi, d)rive")
        user_choice = input(">>> ").lower()
        if user_choice == "q":
            break
        elif user_choice == "c":
            current_taxi = choose_taxi(taxis)
        elif user_choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                total_bill += drive_taxi(current_taxi)
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")

    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    while True:
        taxi_choice = input("Choose taxi: ")
        try:
            taxi_choice = int(taxi_choice)
            if taxi_choice not in range(len(taxis)):
                print("Invalid taxi choice")
                continue
            return taxis[taxi_choice]
        except ValueError:
            print("Invalid taxi choice")


def drive_taxi(taxi):
    distance_to_drive = float(input("Drive how far? "))
    actual_distance_driven = taxi.drive(distance_to_drive)
    if actual_distance_driven == 0:
        print("Not enough fuel to drive")
        trip_cost = 0
    else:
        trip_cost = taxi.get_fare()
        print(f"Your {taxi.name} trip cost you ${trip_cost:.2f}")
    taxi.start_fare()
    return trip_cost


main()
