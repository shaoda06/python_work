# 9-10. Imported Restaurant: Using your latest Restaurant class, store it in
# a module. Make a separate file that imports Restaurant. Make a Restaurant
# instance, and call one of Restaurant’s methods to show that the import
# statement is working properly.


from exercise_9_10_restaurant import Restaurant

my_restaurant = Restaurant('KFC', 'Fried Chicken')
my_restaurant.describe_restaurant()
