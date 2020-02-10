import json


def get_stored_username():
    """Get stored username if available."""
    file_name = "example_10_4_2_username.json"
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
    file_name = "example_10_4_2_username.json"
    with open(file_name, "w") as file_object:
        json.dump(username, file_object)
    return username


def greeting_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We will remember you when you come back, " + username + "!")




greeting_user()
