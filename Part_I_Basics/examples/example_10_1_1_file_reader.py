# 10.1.1 Reading an Entire File
with open('example_10_1_1_pi_digits.txt') as file_object:
    content = file_object.read()
    print(content)
    # Recall that Python's rstrip() method removes, or strips, any whitespace
    # characters from the right side of a string. Now the output matches the
    # contents of the original file exactly
    print(content.rstrip())
