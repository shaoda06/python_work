# A useful tool for working with numerical information is the modulo operator
# (%), which divides one number by another number and returns the remainder:

number = input("Enter a number, and I will tell you if it is even or odd: ")
number = int(number)

if number % 2 == 0:
    result = " is even."
else:
    result = " is odd."

print("\n The number " + str(number) + result)
