import json

file_name = "example_10_4_1_numbers.json"

with open(file_name) as file_object:
    numbers = json.load(file_object)

print(numbers)
