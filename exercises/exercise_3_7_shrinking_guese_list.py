# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.
# • Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.

names = ['MrrNonsense', 'Tony', 'Tom']
msg = " Would u like to have dinner with me?"

print("Hello, " + names[0] + msg)
print("Hello, " + names[1] + msg)
print("Hello, " + names[2] + msg)

print("I just found a bigger dinner table, so now more space is available")
print("I'm considering that invite 3 more people to have dinner together!")

names.insert(0, "James")
names.insert(2, "Josh")
names.append("Leo")

print("Hello again! " + names[0] + msg)
print("Hello again! " + names[1] + msg)
print("Hello again! " + names[2] + msg)
print("Hello again! " + names[3] + msg)
print("Hello again! " + names[4] + msg)
print("Hello again! " + names[5] + msg)

print("emmmm, My new dinner table will not arrive in time for the dinner :(")
print("Now, I can only invite 2 people to the dinner :(")
apologize_msg = ", I am really sorry to tell that I cannot invite you to my dinner."
conform_msg = ", you are still in my invite list, please come to my dinner."
print("Hello " + names.pop() + apologize_msg)
print("Hello " + names.pop() + apologize_msg)
print("Hello " + names.pop() + apologize_msg)
print("Hello " + names.pop() + apologize_msg)
print("Hello " + names[0] + conform_msg)
print("Hello " + names[1] + conform_msg)
del names[0]
del names[0]
print(names)
