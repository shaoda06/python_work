# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.

def make_shirt(size="Large", msg="I Love Python"):
	print("The size will be: " + size)
	print("The text will be: " + msg + "\n")

# making a large shirt with the default message
make_shirt()
# making a medium shirt with the default message
make_shirt("medium")
# making a small shirt with the message reads I love u
make_shirt("small", "I love u")
