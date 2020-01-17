# Importing an Entire Module
import example_8_6_1_pizza


example_8_6_1_pizza.make_pizza(16, 'pepperoni')
example_8_6_1_pizza.make_pizza(
    16,
    'mushrooms',
    'green peppers',
    'extra cheese')


# # Importing Specific Functions
# from example_8_6_1_pizza import make_pizza
#
#
# example_8_6_1_pizza.make_pizza(16, 'pepperoni')
# example_8_6_1_pizza.make_pizza(16, 'mushrooms', 'green peppers',
#                                'extra cheese')
#

# # Using as to Give a Function an Alias
# from example_8_6_1_pizza import make_pizza as mp
#
#
# mp(16, 'pepperoni')
# mp(16, 'mushrooms', 'green peppers', 'extra cheese')
#
#
# # Using as to Give a Module an Alias
# import example_8_6_1_pizza as p
#
#
# p.make_pizza(16, 'pepperoni')
# p.make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')
#
#
# # Importing All Functions in a Module
# from example_8_6_1_pizza import *
#
#
# make_pizza(16, 'pepperoni')
# make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')
