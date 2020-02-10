# 10-11. Favorite Number: Write a program that prompts for the user’s
# favorite number. Use json.dump() to store this number in a file. Write a
# separate program that reads in this value and prints the message, “I know
# your favorite number! It’s _____.”


import json
favorite_number = input("What is you favorite number?")
# favorite_number = int(favorite_number)
file_name = "exercise_10_11_favorite_number.json"
with open(file_name, "w") as file_object:
    json.dump(favorite_number, file_object)
