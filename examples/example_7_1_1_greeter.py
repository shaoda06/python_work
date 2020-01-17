# Writing Clear Prompts
# Each time you use the input() function, you should include a clear,
# easy-to follow prompt that tells the user exactly what kind of information
# you’re looking for. Any statement that tells the user what to enter should
# work. For example:

prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name?\n"

name = input(prompt)
print("\nHello," + name + "!")

# The int() function converts a string representation of a number to a
# numerical representation, as shown here:

age = input("How old are you? ")
age = int(age)
if age >= 18:
    print("You are an adult!")
else:
    print("You are under 18!")
