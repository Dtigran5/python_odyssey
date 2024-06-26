cars = 100  # Total number of cars
space_in_a_car = 4.0  # Passenger capacity per car
drivers = 30  # Number of available drivers
passengers = 90  # Number of passengers
cars_not_driven = cars - drivers  # Cars without drivers
cars_driven = drivers  # Cars driven equals available drivers
carpool_capacity = cars_driven * space_in_a_car  # Total passenger capacity
average_passengers_per_car = passengers / cars_driven  # Average passengers per car

# Displaying transportation information
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car.")
