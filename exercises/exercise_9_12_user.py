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
