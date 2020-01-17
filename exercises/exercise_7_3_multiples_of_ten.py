# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.

number = input("Please enter a number, and I will tell you if it is a "
               "multiple or not.")

number = int(number)

if number >= 10:
    result = " is"
else:
    result = " is not"

print("The number " + str(number) + result + " a multiple.")
