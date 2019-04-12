# Using a Function with a while Loop
def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = first_name + " " + last_name
	return full_name

# This is an infinite loop!
while True:
	print("Please tell me your name: ")
	print("Enter 'quit' to finish.")
	f_name = input("First name: ")
	l_name = input("Last name: ")
	if f_name == "quit" or l_name == "quit":
		break
	else: 
		formatted_name = get_formatted_name(f_name, l_name)
	print("\nHello, " + formatted_name + "!\n")
