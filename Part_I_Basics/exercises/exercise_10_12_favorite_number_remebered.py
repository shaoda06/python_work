# 10-12. Favorite Number Remembered: Combine the two programs from Exercise
# 10-11 into one file. If the number is already stored, report the favorite
# number to the user. If not, prompt for the user’s favorite number and store
# it in a file. Run the program twice to see that it works.

import json
file_name = "exercise_10_11_favorite_number.json"
try:
    with open(file_name) as file_object:
        favorite_number = json.load(file_object)
except FileNotFoundError:
    favorite_number = input("What is your favorite number?")
    with open(file_name, "w") as file_object:
        json.dump(favorite_number, file_object)
else:
    print("I know your favorite number! It’s " + favorite_number + ".")
