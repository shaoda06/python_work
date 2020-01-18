# 10-4. Guest Book: Write a while loop that prompts users for their name. When
# they enter their name, print a greeting to the screen and add a line recording
# their visit in a file called guest_book.txt. Make sure each entry appears on a
# new line in the file.

while True:
    name = input("Please enter your name: \nEnter 'quit' to stop.\n")
    print("Welcome! " + name + ".")
    if name == "quit":
        break
    else:
        file_name = "exercise_10_4_guest_book.txt"
        with open(file_name, "a") as file_object:
            file_object.write(name + "\n")
