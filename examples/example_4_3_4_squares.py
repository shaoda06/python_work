# List Comprehensions
# The approach described earlier for generating the list squares consisted of
# using three or four lines of code. A list comprehension allows you to generate
# this same list in just one line of code.

squares = [value ** 2 for value in range(1, 11)]
print(squares)

# To use this syntax, begin with a descriptive name for the list.
# Next, open a set of square brackets and define the expression for the values you want to store in the new list.
# Then, write a for loop to generate the numbers you want to feed into the expression.
# And, close the square brackets.
# Notice that no colon is used at the end of the for loop.

# Exercise
squares_2 = [value + 2 for value in range(1, 20)]
print(squares_2)

# To create a list stores the even numbers between 1 to 10
even_numbers = [value for value in range(2, 11, 2)]
print(even_numbers)
