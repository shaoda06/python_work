########### Modifying Elements in a List ###########
motorcycles_1 = ['honda', 'yamaha', 'suzuki']
print(motorcycles_1)

motorcycles_1[0] = "ducati"
print(motorcycles_1)

########### Adding Elements to a List ###########

# Appending Elements to the End of a List
motorcycles_2 = ['honda', 'yamaha', 'suzuki']
print(motorcycles_2)

motorcycles_2.append("ducati")
print(motorcycles_2)

# The append() method makes it easy to build lists dynamically
motorcycles_3 = []
motorcycles_3.append('honda')
motorcycles_3.append('yamaha')
motorcycles_3.append('suzuki')
print(motorcycles_3)

# Inserting Elements into a List
motorcycles_4 = ['honda', 'yamaha', 'suzuki']
print(motorcycles_4)
motorcycles_4.insert(0,'ducati')
print(motorcycles_4)

########### Removing Elements from a List ###########

# Removing an Item Using the del Statement
motorcycles_5 = ['honda', 'yamaha', 'suzuki']
print(motorcycles_5)
del motorcycles_5[0]
print(motorcycles_5)

# del motorcycles_5 this command will delete the list itself

# Removing an Item Using the pop() Method - removes the last item
motorcycles_6 = ['honda', 'yamaha', 'suzuki']
print(motorcycles_6)
popped_motorcycle = motorcycles_6.pop()
print(motorcycles_6)
print(popped_motorcycle)

# Popping Item from any Position in a List
motorcycles_7 = ['honda', 'yamaha', 'suzuki']
print(motorcycles_7)
popped_motorcycle = motorcycles_7.pop(0)
print("Popped motorcycle is: "+popped_motorcycle+". Then, the new list is: "+str(motorcycles_7))

# Removing an Item by Value - onlyu the first specified value
motorcycles_8 = ['honda', 'honda', 'suzuki', 'ducati']
print(motorcycles_8)
motorcycles_8.remove('honda')
print(motorcycles_8)

















