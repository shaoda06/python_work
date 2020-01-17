# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
# each person can have more than one favorite number. Then print each person’s
# name along with their favorite numbers.

favorite_numbers = {
    'mrrnonsense': [1, 2, 3, 4],
    'shaoda': [5, 6, 7, 8],
    'xiaoming': [9, 10, 11, 12],
    'icehanba': [13, 14, 15, 16],
    'jyangjun': [17, 18, 19, 20],
}

for name, numbers in favorite_numbers.items():
    print(name.title() + "'s favorite number are: ")
    for number in numbers:
        print("\t" + str(number))
