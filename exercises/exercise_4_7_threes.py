# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.

threes = [value * 3 for value in range(3, 31)]
for value in threes:
    print(value)
