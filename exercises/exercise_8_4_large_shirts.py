# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are
# large by default with a message that reads I love Python. Make a large
# shirt and a medium shirt with the default message, and a shirt of any size
# with a different message.


def make_shirt(size, msg="I love Python!"):
    print("size: " + size)
    print("message: " + msg + "\n")


# making a large shirt with the default message
make_shirt("Large")
# making a medium shirt with the default message
make_shirt("Medium")
# making a small shirt with the message reads I love NY!
make_shirt("Small", msg="I love NY!")
