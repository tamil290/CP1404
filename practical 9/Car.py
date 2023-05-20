class Car:
    def __init__(self, name, fuel):
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def drive(self, distance):
        if distance <= self.fuel:
            self.fuel -= distance
            self.odometer += distance
            return distance  # return the actual distance driven
        else:
            print("Not enough fuel to drive")
            return 0  # if the car can't drive, return 0
