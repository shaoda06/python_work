# 5-10. Checking Usernames: Do the following to create a program that simulates
# how websites ensure that everyone has a unique username.
# • Make a list of five or more usernames called current_users.
# • Make another list of five usernames called new_users. Make sure one or
# two of the new usernames are also in the current_users list.
# • Loop through the new_users list to see if each new username has already
# been used. If it has, print a message that the person will need to enter a
# new username. If a username has not been used, print a message saying
# that the username is available.
# • Make sure your comparison is case insensitive. If 'John' has been used,
# 'JOHN' should not be accepted.

current_users = ['Shaoda','MrrNonsense','jyangjun','xiaoming','admin']
new_users = ['lilmrrnonsense','z495118541','z940607','shaoda','bestshooter']

current_users_insensitive = []
for current_user in current_users:
	current_users_insensitive.append(current_user.lower())
for new_user in new_users:
	if new_user.lower() in current_users_insensitive:
		print("Sorry, the username: \"" + new_user + "\" has been used.")
	else:
		print("Congratulations! the username: \"" + new_user + "\" is available.")
