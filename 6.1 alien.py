# Consider a game featuring aliens that can have different colors and point
# values. This simple dictionary stores information about a particular alien:
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# Accessing Values in a Dictionary
new_points = alien_0['points']
print("You just earned " + str(new_points) + " ponits!")

# Adding New Key-Value Pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with an Empty Dictionary
alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = 5
print(alien_1)

# Modifying Values in a Dictionary
alien_2 = {'color': 'green'}
print("The alien is " + alien_2['color'] + ".")

alien_2['color'] = 'yellow'
print("The alien is now " + alien_2['color'] + ".")

alien_3 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Orginal x-position: " + str(alien_3['x_position']))

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.

if alien_3['speed'] == 'slow':
	x_increment = 1
elif alien_3['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3
	
# The new position is the old position plus the increment.
alien_3['x_position'] = alien_3['x_position'] + x_increment

print("New x-position: " + str(alien_3['x_position']))

# Removing Key-Value Pairs
alien_4 = {'color': 'green', 'points': 5}
print(alien_4)

del alien_4['points']
print(alien_4)

