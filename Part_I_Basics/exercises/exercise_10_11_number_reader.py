import json
file_name = "exercise_10_11_favorite_number.json"
with open(file_name) as file_object:
    favorite_number = json.load(file_object)
print("I know your favorite number! It’s " + favorite_number + ".")