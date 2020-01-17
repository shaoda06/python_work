# 7-2. Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group. If the answer is more than eight, print a
# message saying they’ll have to wait for a table. Otherwise, report that
# their table is ready.

people_number = input("How many people are in your dinner group?")
people_number = int(people_number)

if people_number > 8:
    print("You will have to wait for a table.")
else:
    print("Your table is ready.")
