# use a for loop to print out each name in a list of magicians
magicians = ['alice','david','carolina']
for magician in magicians:
	print(magician)
# Doing More Work Within a for Loop
for magician in magicians:
	print(magician.title()+", that was a great trick!")
	print("I can't wait to see your next trick, "+magician.title()+".\n")
# Doing Something After a for Loop
print("Thank you, everyone. That was a great magic show!")
