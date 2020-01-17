# 3.3.1 Sorting a List Permanently with the sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
# The following example sorts the list of cars in reverse alphabetical order:
cars.sort(reverse=True)
print(cars)

# 3.3.2 Sorting a List Temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is teh original list: ")
print(cars)

print("\nHere is the sorted list: ")
print(sorted(cars, reverse=True))

print("\nHere is the original list again: ")
print(cars)

# 3.3.3 Printing a List in Reverse Order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

# 3.3.4 Finding the Length of a List
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
