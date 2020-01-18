# 10.3.5 Handing the FileNotFoundError Exception
file_name = "alice.txt"

# with open(file_name) as file_object:
#     contents = file_object.read()

try:
    with open(file_name) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = "Sorry, the file" + file_name + " does not exist."
    print(msg)
