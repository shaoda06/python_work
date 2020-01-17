# 9-14. Dice: The module random contains functions that generate random numbers
# in a variety of ways. The function randint() returns an integer in the
# range you provide. The following code returns a number between 1 and 6:
#
# from random import randint
# x = randint(1, 6)
#
# Make a class Die with one attribute called sides, which has a default
# value of 6. Write a method called roll_die() that prints a random number
# between 1 and the number of sides the die has. Make a 6-sided die and roll
# it 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.


from random import randint


class Die:
    """A simple attempt to represent dices."""

    def __init__(self, sides=6):
        """Initialize attribute sides to receive a number to decide how many
        sides the die has. Default value is 6. """
        self.sides = sides

    def roll_die(self):
        result = randint(1, self.sides)
        return result


hexahedron = Die()
decahedron = Die(10)
icosahedron = Die(20)

print("10 results of rolling a hexahedron dice (6 sides): ")
for count in range(10):
    print(str(count + 1) + ": " + str(hexahedron.roll_die()))

print("\n10 results of rolling a decahedron(10 sides): ")
for count in range(10):
    print(str(count + 1) + ": " + str(decahedron.roll_die()))

print("\n10 results of rolling a icosahedron(20 sides): ")
for count in range(10):
    print(str(count + 1) + ": " + str(icosahedron.roll_die()))
