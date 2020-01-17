# 9-3. Users: Make a class called User. Create two attributes called
# first_name and last_name, and then create several other attributes that are
# typically stored in a user profile. Make a method called describe_user()
# that prints a summary of the user’s information. Make another method called
# greet_user() that prints a personalized greeting to the user. Create
# several instances representing different users, and call both methods for
# each user.


class User:
    def __init__(self, first_name, last_name, age, gender):
        """initialize first_name, last_name, age and gender attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        """print a summary of the user's information"""
        print("First name: " + self.first_name)
        print("Last name: " + self.last_name)
        print("Age: " + str(self.age))
        print("Gender: " + self.gender)

    def greet_user(self):
        """print a personalized greeting to the user"""
        print(
            "Welcome! " +
            self.first_name.title() +
            " " +
            self.last_name.title())


# Creating individual instances from User
user_0 = User("f0", "l0", "a0", "g0")
user_1 = User("f1", "l1", "a1", "g1")
user_2 = User("f2", "l2", "a2", "g2")

# Calling both methods in User for each instance
user_0.describe_user()
user_0.greet_user()

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()
