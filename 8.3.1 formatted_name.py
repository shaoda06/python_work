# Returning a Simple Value
def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = first_name + " " + last_name
	return full_name.title()

musician = get_formatted_name("shaoda", "liu")
print(musician)

# Making an argument optional
def get_formatted_name_1(first_name, last_name, middle_name=""):
	"""Return a full name, neatly formatted."""
	if middle_name:
		full_name = first_name + " " + middle_name + " " + last_name
	else:
		full_name = first_name + " " + last_name
	return full_name.title()

musician = get_formatted_name_1("shaoda", "liu", "emmmm")
print(musician)
musician = get_formatted_name_1("shaoda", "liu",)
print(musician)
	
