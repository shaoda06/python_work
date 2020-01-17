# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.

person_0 = {
    'first_name': 'lei',
    'last_name': 'li',
    'age': 30,
    'city': 'beijing',
}

person_1 = {
    'first_name': 'san',
    'last_name': 'zhang',
    'age': 26,
    'city': 'tianjin',
}

person_2 = {
    'first_name': 'si',
    'last_name': 'li',
    'age': 28,
    'city': 'guangzhou',
}

people = [person_0, person_1, person_2]

for person in people:
    for key, value in person.items():
        print(key + ": " + str(value))

for person in people:
    full_name = person['first_name'].title() + " " + person['last_name'].title()
    age = person['age']
    location = person['city'].title()
    print(full_name + " is " + str(age) + " years old lives in " + location
          + ".")
