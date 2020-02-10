import json

file_name = "example_10_4_2_username.json"

with open(file_name) as file_object:
    username = json.load(file_object)
    print("Welcome back, " + username + "!")
