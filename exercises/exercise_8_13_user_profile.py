# 8-13. User Profile: Start with a copy of user_profile.py from page 153.
# Build a profile of yourself by calling build_profile(), using your first
# and last names and three other key-value pairs that describe you.


def build_profile(first, last, **user_info):
    """Build a dictionary containing my information"""
    profile = {
        'first_name': first,
        'last_name': last
    }

    for key, value in user_info.items():
        profile[key] = value
    return profile


my_profile = build_profile('shadao', 'liu',
                           location='mcallen',
                           hometown='tianjin',
                           age='25')

print('This is all the information we have in profile: ')
for key, value in my_profile.items():
    print(key.title() + ": " + value.title())
