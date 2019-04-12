# 7-10. Dream Vacation: Write a program that polls users about their dream
# vacation. Write a prompt similar to If you could visit one place in the world,
# where would you go? Include a block of code that prints the results of the poll.

prompt = "If you could visit one place in the world, where would you go? "
prompt += "\nEnter 'quit' to finish.\n"

locations = []
location = ""

while location != "quit":
	location = input(prompt)
	if location != "quit":
		locations.append(location)

print("The locations you want to visit: ")
for location in locations:
	print(location)
