# For example, if we have a rectangle that should always be a certain size,
# we can ensure that its size doesn’t change by putting the dimensions into a
# tuple
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

# Looping Through All Values in a Tuple

for dimension in dimensions:
	print(dimension)
	
# Writing over a Tuple
dimensions = (400,100)

for dimension in dimensions:
	print(dimension)
