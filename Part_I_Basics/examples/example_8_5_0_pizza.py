# Passing an Arbitrary Number of Arguments

# For example, consider a function that builds a pizza. It needs to accept a
# number of toppings, but you can’t know ahead of time how many toppings
# a person will want.


def make_pizza(*toppings):
    """Summarize the pizza we are about to make"""
    print("Making a pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)
    print()


make_pizza('peperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# Mixing Positional and Arbitrary Arguments
# If you want a function to accept several different kinds of arguments, the
# parameter that accepts an arbitrary number of arguments must be placed
# last in the function definition. Python matches positional and keyword
# arguments first and then collects any remaining arguments in the final
# parameter.

def make_pizza_2(size, *toppings):
    """Summarize the pizza we are about to make"""
    print("Making a " + str(size) + "-inch pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)
    print()


make_pizza_2(16, 'pepperoni')
make_pizza_2(12, 'mushrooms', 'green peppers', 'extra cheese')
