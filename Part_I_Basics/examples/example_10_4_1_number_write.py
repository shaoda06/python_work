# 10.4.1 Using json.dump() and json.load()

import json

numbers = [2, 3, 5, 11, 13]

file_name = "example_10_4_1_numbers.json"

with open(file_name, "w") as file_object:
    json.dump(numbers, file_object)
