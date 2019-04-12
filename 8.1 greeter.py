# Here is a simple function named greet_user() taht prints a greeting:

def greet_user():
	# The text is a conmment called a docstring, which describes what
	# the function dose. Docstrings are enclosed in triple quotes, which
	# Python looks for when it generates documentation for the functions
	# in your programs.
	"""Display a simple greeting."""
	print("Hello!")
	
greet_user()
print(greet_user.__doc__)

# Passing Information to a Function
def greet_user(username):
	"""Display a simple greeting.
	
	passing information to a function
	in other word, to display username"""
	print("Hello, " + username.title() + "!")

greet_user("shaoda")
