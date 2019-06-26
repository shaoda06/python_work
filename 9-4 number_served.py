# 9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
# Add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new number and
# print the value again.
# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any number
# you like that could represent how many customers were served in, say, a
# day of business.


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Restaurant name is: " + self.restaurant_name.title())
        print("Cuisine type is: " + self.cuisine_type)

    def open_restaurant(self):
        print("Our restaurant now is open!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number_served):
        self.number_served += number_served


# Create an instance from Class Restaurant
new_restaurant = Restaurant('KFC', 'Fried Chicken')
# Change the value of number served directly
new_restaurant.number_served = 10
print("Number Served: " + str(new_restaurant.number_served))
# Change the value of number served through method set_number_served()
new_restaurant.set_number_served(15)
print("Number Served: " + str(new_restaurant.number_served))
# Increment the number of customers who have been served a day.
new_restaurant.increment_number_served(20)
print("Number Served: " + str(new_restaurant.number_served))
