# 9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 166). Write a method called increment_
# login_attempts() that increments the value of login_attempts by 1. Write
# another method called reset_login_attempts() that resets the value of
# login_ attempts to 0. Make an instance of the User class and call
# increment_login_attempts() several times. Print the value of login_attempts
# to make sure it was incremented properly, and then call
# reset_login_attempts(). Print login_attempts again to make sure it was
# reset to 0.


class User:
    def __init__(self, first_name, last_name, age, gender):
        """initialize first_name, last_name, age and gender attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


new_user = User('shaoda', 'liu', 25, 'male')
new_user.greet_user()
print(new_user.login_attempts)

new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
new_user.increment_login_attempts()
print(new_user.login_attempts)

new_user.reset_login_attempts()
print(new_user.login_attempts)
