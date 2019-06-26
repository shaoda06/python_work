# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote
# in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
# the class will work; just pick the one you like better. Add an attribute called
# flavors that stores a list of ice cream flavors. Write a method that displays
# these flavors. Create an instance of IceCreamStand, and call this method.


class Restaurant:
    """A simple attempt to represent a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant name is: " + self.restaurant_name.title())
        print("Cuisine type is: " + self.cuisine_type)

    def open_restaurant(self):
        print("Our restaurant now is open!")


class IceCreamStand(Restaurant):
    """Represent aspect a restaurant, specific to ice cream stands."""

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize attributes of parent class
        Then initialize attributes specific to an ice cream stand
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'banana', 'vanilla']

    def display_flavors(self):
        """Display served flavors"""
        print("These are all the flavors served: ")
        for flavor in self.flavors:
            print(flavor)


new_ice_cream_stand = IceCreamStand("Ice World", "Ice Cream Only")
new_ice_cream_stand.display_flavors()
