# 10.1.6 Large Files: One Million Digits
file_name = "example_10_1_6_pi_million_digits.txt"

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))
