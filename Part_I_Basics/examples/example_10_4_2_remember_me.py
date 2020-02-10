# 10.4.2 Saving and Reading User-Generated Data

import json

username = input("What is your name: ")

file_name = "example_10_4_2_username.json"
with open(file_name, "w") as file_object:
    json.dump(username, file_object)
    print("We will remember you when you come back, " + username + "!")
