# 9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
# Add a method to the Battery class called upgrade_battery(). This method
# should check the battery size and set the capacity to 85 if it isn’t already.
# Make an electric car with a default battery size, call get_range() once, and
# then call get_range() a second time after upgrading the battery. You should
# see an increase in the car’s range.


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
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range) + " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        self.battery_size = 85


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


my_electric_car = ElectricCar('tesla', 'model S', 2016)
my_electric_car.battery.get_range()
my_electric_car.battery.upgrade_battery()
my_electric_car.battery.get_range()
