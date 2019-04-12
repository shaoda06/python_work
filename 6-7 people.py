# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.

person_0 = {
	'first_name': 'Shaoda',
	'last_name': 'Liu',
	'age': 25,
	'city': 'McAllen',
	}

person_1 = {
	'first_name': 'Ming',
	'last_name': 'Yang',
	'age': 26,
	'city': 'Tianjin',
	}

person_2 = {
	'first_name': 'Jie',
	'last_name': 'Meng',
	'age': 28,
	'city': 'Leipzig',
	}

people = [person_0, person_1, person_2]

for person in people:
	print("\nFull name: " + person['first_name'] + " " + person['last_name'])
	print("Age: " + str(person['age']))
	print("Location: " + person['city'])
