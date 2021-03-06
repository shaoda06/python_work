favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name, language in favorite_languages.items():
    print(name.title() + " favorite language is " +
          language.title() + ".")

# Looping Through All the Keys in a Dictionary
friends = ['phil', 'sarah', 'erin']
for name in friends:
    if name in favorite_languages.keys():
        print("Hi, " + name + "! I see your favorite language is: " +
              favorite_languages[name].title())
    else:
        print("Hi, " + name + "! Please take our poll!")

# Looping Through a Dictionary’s Keys in Order
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll!")

# Looping Through All Values in a Dictionary
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# When you wrap set() around a list that contains duplicate items, 
# Python identifies the unique items in the list and builds a set 
# from those items.
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
