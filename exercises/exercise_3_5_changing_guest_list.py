# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# • Start with your program from Exercise 3-4. Add a print statement at the
# end of your program stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still
# in your list.

names = ['MrrNonsense', 'Tony', 'Tom']
msg = " Would u like to have dinner with me?"

print("Hello, " + names[0] + msg)
print("Hello, " + names[1] + msg)
print("Hello, " + names[2] + msg)

print(names[0] + " can not come to dinner.")

names[0] = "James"
print("Hello, " + names[0] + msg)
print("Hello, " + names[1] + msg)
print("Hello, " + names[2] + msg)
