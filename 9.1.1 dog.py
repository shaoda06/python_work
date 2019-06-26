class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")


# Making an instance from a class
my_dog = Dog('Tom', 3)

# Accessing Attributes
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# Calling Methods
my_dog.sit()
my_dog.roll_over()

# Creating Multiple Instances
your_dog = Dog('lucy', 6)
print("Your dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
