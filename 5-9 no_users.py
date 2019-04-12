# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
# not empty.
# • If the list is empty, print the message We need to find some users!
# • Remove all of the usernames from your list, and make sure the correct
# message is printed.

# usernames = ['shaoda','MrrNonsense','jyangjun','xiaoming','admin']
usernames = []
generic_greeting = " thank you for logging in again."
special_greeting = "would you like to see a status report?"
if usernames:
	for username in usernames:
		if username == "admin":
			print("Hello " + username + special_greeting)
		else:
			print("Hello " + username + generic_greeting)
else:
	print("We need to find some users!")
