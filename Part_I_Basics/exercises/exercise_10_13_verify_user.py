# 10-13. Verify User: The final listing for remember_me.py assumes either
# that the user has already entered their username or that the program is
# running for the first time. We should modify it in case the current user is
# not the person who last used the program. Before printing a welcome back
# message in greet_user(), ask the user if this is the correct username. If
# it’s not, call get_new_username() to get the correct username.

import json


def get_stored_username():
    """Get stored username if available."""
    file_name = "exercise_10_13_verify_user.json"
    try:
        with open(file_name) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name: ")
    file_name = "exercise_10_13_verify_user.json"
    with open(file_name, "w") as file_object:
        json.dump(username, file_object)
    return username


def greeting_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        msg = "Please enter y/n to verify that '" + username + "' is correct."
        verification = input(msg)
        if verification == "y":
            print("Welcome back, " + username + "!")
        else:
            username = get_new_username()
            print("We will remember you when you come back, " + username + "!")
    else:
        username = get_new_username()
        print("We will remember you when you come back, " + username + "!")




greeting_user()

