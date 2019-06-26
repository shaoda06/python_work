# 9.2.1 The Car Class
# Let’s write a new class representing a car. Our class will store information
# about the kind of car we’re working with, and it will have a method that
# summarizes this information:

# 9.2.2 Setting default value for an attribute
# Line #24 is to initialize attribute with a default value 0
# Line #31 is to add a method to read each car's odometer
# Line #50 is to call the method to read specified car's odometer

# 9.2.3 Modifying attribute values
# Line #52 is to modifying attribute's value directly
# Line #55 is to modifying attribute's value through a method
# Line #61 is to incrementing an attribute's value through a method


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to represent a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Modify odometer through a method and make sure no one is able to roll back the odometer reading"""
        if mileage < self.odometer_reading:
            print("You can't roll back an odometer!")
        else:
            self.odometer_reading = mileage

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

print(my_new_car.read_odometer())

my_new_car.odometer_reading = 23
print(my_new_car.read_odometer())

my_new_car.update_odometer(46)
print(my_new_car.read_odometer())

my_new_car.update_odometer(23)
print(my_new_car.read_odometer())

my_new_car.increment_odometer(100)
my_new_car.read_odometer()
