# 8-5. Cities: Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the
# default country.

def describe_city(city="reykjavik", country="iceland"):
	print(city.title() + " is in " + country.title() + ".\n")
	
describe_city("Tianjin","China")
describe_city(city="tianjin", country="china")
describe_city(country="china", city="tianjin")
