# The following example sends a list of names to a function called greet_users()
# which greets each person in the list individually


def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"


user_names = ['hannah', 'ty', 'margot']
greet_users(user_names)
