# Defining a Tuple
# A tuple looks just like a list except you use parentheses instead of square
# brackets. Once you define a tuple, you can access individual elements by
# using each item’s index, just as you would for a list.

# For example, if we have a rectangle that should always be a certain size,
# we can ensure that its size does not change by putting the dimensions into a
# tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Looping Through All Values in a Tuple

for dimension in dimensions:
    print(dimension)

# Writing over a Tuple
# Although you can’t modify a tuple, you can assign a new value to a variable
# that holds a tuple. So if we wanted to change our dimensions, we could
# redefine the entire tuple:
dimensions = (400, 100)

for dimension in dimensions:
    print(dimension)
