# Copying a List
# For example, imagine we have a list of our favorite foods and want to
# make a separate list of foods that a friend likes. This friend likes everything
# in our list so far, so we can create their list by copying ours:

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
