# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant name is: " + self.restaurant_name.title())
        print("Cuisine type is: " + self.cuisine_type)

    def open_restaurant(self):
        print("Our restaurant now is open!")


# Creating 3 individual instances
restaurant_1 = Restaurant("restaurant 1", "type 1")
restaurant_2 = Restaurant("restaurant 2", "type 2")
restaurant_3 = Restaurant("restaurant 3", "type 3")

# Calling describe_restaurant() for each instance
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
