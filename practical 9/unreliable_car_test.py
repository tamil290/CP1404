from unreliable_car import UnreliableCar

# Create a new UnreliableCar object
my_car = UnreliableCar("My Car", 100, 50)

# Print the car's details
print(my_car)  # Output: Car: My Car, Fuel: 100, Reliability: 50

distance_driven = my_car.drive(50)
print("Distance driven:", distance_driven)