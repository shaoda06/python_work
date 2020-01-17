# 7-5. Movie Tickets: A movie theater charges different ticket prices
# depending on a person’s age. If a person is under the age of 3, the ticket
# is free; if they are between 3 and 12, the ticket is $10; and if they are
# over age 12, the ticket is $15. Write a loop in which you ask users their
# age, and then tell them the cost of their movie ticket.

prompt = "\nPlease enter your age: "

# using conditional test
# age = ""
# while age != "quit":
# age = input(prompt)
# if age != "quit":
# age = int(age)
# if age < 3:
# price = 0
# elif age < 12:
# price = 10
# else:
# price = 15
# print("The ticket price is: $" + str(price) + ".")

# using active as flag variable
active = True
while active:
    age = input(prompt)
    if age != "quit":
        age = int(age)
        if age < 3:
            price = 0
        elif age < 12:
            price = 10
        else:
            price = 15
        print("The ticket price is: $" + str(price) + ".")
    else:
        active = False

# using break statement
# while True:
# age = input(prompt)
# if age != "quit":
# age = int(age)
# if age < 3:
# price = 0
# elif age < 12:
# price = 10
# else:
# price = 15
# print("The ticket price is: $" + str(price) + ".")
# else:
# break
