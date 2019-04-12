# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
# statement to the end of your program informing people that you found a
# bigger dinner table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.

names = ['shaoda','xuanxuan','xiaoming']
msg = " Would u like to have dinner with me?"

print("Hello, "+names[0]+msg)
print("Hello, "+names[1]+msg)
print("Hello, "+names[2]+msg)

print("I just found a bigger dinner table, so now more space is available")
print("I'm considering that invite 3 more people to have dinner together!")

names.insert(0,"Tony")
names.insert(2,"xiaoli")
names.append("xiaobai")

print("Hello again! "+names[0]+msg)
print("Hello again! "+names[1]+msg)
print("Hello again! "+names[2]+msg)
print("Hello again! "+names[3]+msg)
print("Hello again! "+names[4]+msg)
print("Hello again! "+names[5]+msg)
