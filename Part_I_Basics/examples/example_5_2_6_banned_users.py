banned_users = ['andrew', 'carolina', 'david']
user = "andrew"
# Checking Whether a Value Is in a List
if user in banned_users:
    print(
        user.title() + ", you cannot post a response because you are in the banned list.")

user = "tony"
# Checking Whether a Value Is Not in a List
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
