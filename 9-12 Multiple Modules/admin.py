from user import User


class Privilege:
    """A simple attempt to represent privileges"""

    def __init__(self):
        """Initialize attributes for privileges"""
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("Administrator has privileges bellow: ")
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    """Represent aspect a user, specific to administrators"""

    def __init__(self, first_name, last_name, age, gender):
        """
        Initialize attributes of parent class
        Then initialize attributs specific to administrator
        """
        super().__init__(first_name, last_name, age, gender)
        self.privilege = Privilege()
