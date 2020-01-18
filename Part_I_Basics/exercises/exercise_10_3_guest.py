# 10-3. Guest: Write a program that prompts the user for their name. When they
# respond, write their name to a file called guest.txt.
file_name = "exercise_10_3_guest.txt"
names = ""
while True:
    name = input("Please enter your name:\n- Or enter 'quit' to stop.")
    if name == "quit":
        break
    else:
        names = names + name + "\n"

with open(file_name, "w") as file_object:
    file_object.write(str(names))
