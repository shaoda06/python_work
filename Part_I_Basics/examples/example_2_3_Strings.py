# 2.3.1 Changing Case in a String with Methods
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

# 2.3.2 Combining or Concatenating Strings
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")

message = "Hello, " + full_name.title() + "!"
print(message)

# 2.3.3 Adding Whitespace to Strings with Tabs or Newlines
# To add a tab to your text, use the character combination \t as shown
print("Python")
print("\tPython")

# To add a newline in a string, use the character combination \n:
print("Languages: \nPython\nC\nJavaScript")

# Combine tabs and newlines in a single string
print("Languages: \n\tPython\n\tC\n\tJavaScript")

# 2.3.4 Stripping Whitespace
favorite_language = "Python "
print(favorite_language)
print(favorite_language.rstrip())

favorite_language = " Python "
print(favorite_language)
favorite_language = favorite_language.rstrip()
favorite_language = favorite_language.lstrip()
print(favorite_language)

# 2.3.5 Avoiding Syntax Errors with Strings
message = "One of Python's strengths is its diverse community."
print(message)
message = 'One of Python\'s strengths is its diverse community.'
print(message)
