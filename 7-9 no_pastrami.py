# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.

sandwich_orders = ['sandwich 01', 'pastrami', 'sandwich 02', 'sandwich 03', 'pastrami','pastrami']

print("The deli has run out of pastrami!")

target = "pastrami"
while target in sandwich_orders:
	sandwich_orders.remove(target)
	
print(sandwich_orders)
	
