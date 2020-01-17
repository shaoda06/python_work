"""A set of classes used to represent gas and electric cars."""
from example_9_4_6_car import Car


class Battery:
    def __init__(self, battery_size=70):
        """A simple attempt to model a battery for an electric car"""
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-KWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            max_range = 240
        elif self.battery_size == 85:
            max_range = 270
        message = "This car can go approximately " + str(max_range) \
                  + " miles on a full charge."
        print(message)


class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
