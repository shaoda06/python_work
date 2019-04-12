# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.

number = input("Please enter a number, and I will tell you if it is a"
				+ "mutiple of 10 or not: ")
number = int(number)

if number % 10 == 0:
	print("YES!")
else:
	print("NO!")
