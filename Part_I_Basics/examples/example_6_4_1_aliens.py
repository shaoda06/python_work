# Nesting

# Sometimes you’ll want to store a set of dictionaries in a list or a list of
# items as a value in a dictionary. This is called nesting.

# A List of Dictionaries
# the following code builds a list of three aliens:

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(aliens)

# more realistic example would involve more than three aliens with
# code that automatically generates each alien. In the following example we
# use range() to create a fleet of 30 aliens:

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# to change the first three aliens to yellow,
# medium-speed aliens worth 10 points each
for alien in aliens[0:3]:
    # if alien['color'] == 'green':
    #     alien['color'] = 'yellow'
    #     alien['speed'] = 'medium'
    #     alien['points'] = 10
    alien['color'] = 'yellow'
    alien['speed'] = 'medium'
    alien['points'] = 10

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print("\nTotal number of aliens: " + str(len(aliens)))
