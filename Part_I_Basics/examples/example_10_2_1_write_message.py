# 10.2.1 Writing to an Empty File
file_name = "example_10_2_1_programming.txt"

with open(file_name, "w") as file_object:
    file_object.write("I love programming.")

# Python can only write strings to a text file. If you want to store
# numerical data in a text file, you’ll have to convert the data to string
# format first using the str() function.

# 10.2.2 Writing Multiple Lines
# If you open programming.txt, you will see the two lines squished together.
with open(file_name, "w") as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")

# Including newlines in your write() statement makes each string appear on its
# own line
with open(file_name, "w") as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# 10.3.3 Appending to a File
with open(file_name,"a") as file_object:
    file_object.write("I also love finding meaning in large dataset. \n")
    file_object.write("I love creating apps that can run in a browser.\n")
