# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.


class User:
    def __init__(self, first_name, last_name, age, gender):
        """initialize first_name, last_name, age and gender attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        """print a summary of the user's information"""
        print("-------- Personal Information --------")
        print("First name: " + self.first_name)
        print("Last name: " + self.last_name)
        print("Age: " + self.age)
        print("Gender: " + self.gender)
        print("--------------------------------------")

    def greet_user(self):
        """print a personalized greeting to the user"""
        print("Hello " + self.first_name + " " + self.last_name + "! Thank you for using our system! ")


# Creating individual instances from User
user1 = User("First1", "Last1", "10", "Male")
user2 = User("First2", "Last2", "20", "Male")
user3 = User("First3", "Last3", "30", "Male")
user4 = User("First4", "Last4", "40", "Female")
user5 = User("First5", "Last5", "50", "Female")

# Calling both methods in User for each instance
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

user4.describe_user()
user4.greet_user()

user5.describe_user()
user5.greet_user()
