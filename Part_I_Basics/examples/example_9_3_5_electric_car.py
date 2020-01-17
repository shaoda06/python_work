# Instances as Attributes


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
        """Modify odometer through a method and make sure no one is able to
        roll back the odometer reading """
        if mileage < self.odometer_reading:
            print("You can't roll back an odometer!")
        else:
            self.odometer_reading = mileage

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("Gas tank has been filled!")


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
    """Represent aspects a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    # Overriding Methods from the Parent Class
    def fill_gas_tank(self):
        """Electric cars don't have gas tank."""
        print("This car doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
