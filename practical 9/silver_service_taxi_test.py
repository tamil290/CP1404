from silver_service_taxi import SilverServiceTaxi

# create a new SilverServiceTaxi called "Fancy Taxi", with 100 units of fuel, and fanciness of 2
fancy_taxi = SilverServiceTaxi("Fancy Taxi", 100, 2)

# drive the taxi 18km
fancy_taxi.drive(18)

# print the taxi's details and the current fare
print(fancy_taxi)
print(f"Current Fare: ${fancy_taxi.get_fare():.2f}")
