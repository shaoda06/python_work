# Slicing a List
# To make a slice, you specify the index of the first and last elements

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

# Looping Through a Slice
print("Here are the first three players on my team: ")
for player in players[:3]:
    print(player)
