# 10-6. Addition: One common problem when prompting for numerical input
# occurs when people provide text instead of numbers. When you try to convert
# the input to an int, you’ll get a TypeError. Write a program that prompts
# for two numbers. Add them together and print the result. Catch the
# TypeError if either input value is not a number, and print a friendly error
# message. Test your program by entering two numbers and then by entering
# some text instead of a number.

prompts = "Please enter two numbers, and I will add them together."
first_number = input("First number: ")
second_number = input("Second number: ")
try:
    first_number = int(first_number)
    second_number = int(second_number)
except ValueError:
    print("You can only enter intergers.")
else:
    sum = first_number + second_number
    print(str(first_number) + " + " + str(second_number) + " = " + str(sum))
