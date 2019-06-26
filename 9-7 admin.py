# 9-7. Admin: An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
# or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
# of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin, and call your method.


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


class Admin(User):
    """Represent aspect a user, specific to administrators"""

    def __init__(self, first_name, last_name, age, gender):
        """
        Initialize attributes of parent class
        Then initialize attributs specific to administrator
        """
        super().__init__(first_name, last_name, age, gender)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("Administrator has privileges bellow: ")
        for privilege in self.privileges:
            print(privilege)


admin = Admin('shaoda', 'liu', 25, 'male')
admin.show_privileges()