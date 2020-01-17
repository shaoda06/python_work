# 8-6. City Names: Write a function called city_country() that takes in the
# name of a city and its country. The function should return a string
# formatted like this: "Santiago, Chile" Call your function with at least
# three city-country pairs, and print the value that’s returned.


def city_country(name, country):
    formatted_string = name.title() + ", " + country.title()
    return formatted_string


print(city_country("tianjin", "china"))
print(city_country("beijing", "china"))
print(city_country("guangzhou", "china"))
