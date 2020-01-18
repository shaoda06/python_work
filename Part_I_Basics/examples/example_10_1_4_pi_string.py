# 10.1.4 Making a List of Lines from a File
file_name = "example_10_1_1_pi_digits.txt"

with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
