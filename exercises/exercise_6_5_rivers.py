# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# • Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary.

rivers = {
    'mississippi river': 'united states',
    'nile': 'egypt',
    'haihe': 'china',
}

for river_name, river_country in rivers.items():
    print("The " + river_name.title() + " runs through " + river_country.title()
          + ".\n")

print("Rivers names: ")
for river_name in rivers.keys():
    print(river_name.title())

print("\nCity names: ")
for river_country in rivers.values():
    print(river_country.title())
