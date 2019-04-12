# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# • Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary.

rivers = {
	'huanghe': 'china',
	'nile': 'egypt',
	'haihe': 'tianjin',
	}

for river_name, city_name in rivers.items():
	print("The " + river_name + " runs through " + city_name + ".\n")

print("Rivers names: ")
for river_name in rivers.keys():
	print(river_name)

print("\nCity names: ")
for city_name in rivers.values():
	print(city_name)
