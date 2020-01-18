# 10.3.6 Analyzing Text
file_name = "example_10_3_6_alice.txt"

try:
    with open(file_name) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = "Sorry, the file " + file_name + " dose not exist."
    print(msg)
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print("The file " + file_name + " has about " + str(num_words) + " words.")
