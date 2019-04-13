# Importing an Entire Module
# import pizza

# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')

# Importing Specific Functions
# from pizza import making_pizzas

# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')

# Using as to Give a Function an Alias
# from pizza import make_pizza as mp
# mp(16, 'pepperoni')
# mp(16, 'mushrooms', 'green peppers', 'extra cheese')

# Using as to Give a Module an Alias
# import pizza as p
# p.make_pizza(16, 'pepperoni')
# p.make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')

# Importing All Functions in a Module
from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(16, 'mushrooms', 'green peppers', 'extra cheese')