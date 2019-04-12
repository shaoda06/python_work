# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.


prompt = "Please enter a pizza topping you want to add.\n"
prompt += "Enter 'quit' to finish.\n"

pizza_topping = ""

# using conditional test
# while pizza_topping != "quit":
	# pizza_topping = input(prompt)
	# if pizza_topping != "quit":
		# print("You will add " + pizza_topping + " to your pizza!\n")
		
# using active variable
# active = True
# while active:
	# pizza_topping = input(prompt)
	# if pizza_topping != "quit":
		# print("You will add " + pizza_topping + " to your pizza!\n")
	# else:
		# active = False
		
# using a break statement
while True:
	pizza_topping = input(prompt)
	if pizza_topping != "quit":
		print("You will add " + pizza_topping + " to your pizza!\n")
	else:
		break
