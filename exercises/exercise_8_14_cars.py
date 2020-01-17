# 8-14. Cars: Write a function that stores information about a car in a
# dictionary. The function should always receive a manufacturer and a model
# name. It should then accept an arbitrary number of keyword arguments. Call
# the function with the required information and two other name-value pairs,
# such as a color or an optional feature. Your function should work for a
# call like this one: car = make_car('subaru', 'outback', color='blue',
# tow_package=True) Print the dictionary that’s returned to make sure all the
# information was stored correctly.


def car_info(manufacturer, model, **other_info):
    """
        Build a car profile containing its manufacturer,
        model name and some other information
    """
    car = {
        "manufacturer": manufacturer,
        "model": model,
    }
    for key, value in other_info:
        car[key] = value
    return car


car = car_info("BMW", "z4", color="red", energy="gasoline")

print('This is all the information we have in profile: ')
for key, value in car.items():
    print(key.title() + ": " + value.title())
