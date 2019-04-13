# 8-14. Cars: Write a function that stores information about a car in a dictionary.
# The function should always receive a manufacturer and a model name. It
# should then accept an arbitrary number of keyword arguments. Call the function
# with the required information and two other name-value pairs, such as a
# color or an optional feature. Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was
# stored correctly.


def build_car(manufacturer, model_name, **car_info):
    """
    Build a car profile containing its manufacturer,
    model name and some other information
    """
    car_profile = {
        'manufacturer': manufacturer,
        'model_name': model_name,
    }
    for key, value in car_info.items():
        car_profile[key] = value
    return car_profile


car = build_car('bmw', 'z4', color='black', other_feature="other feature 1")

print('This is all the information we have in profile: ')
for key, value in car.items():
    print(key.title() + ": " + value.title())
