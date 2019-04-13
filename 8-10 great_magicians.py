# 8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
# Write a function called make_great() that modifies the list of magicians by adding
# the phrase the Great to each magician’s name. Call show_magicians() to
# see that the list has actually been modified.


def make_great(magicians):
    for count in range(0, len(magicians)):
        magicians[count] = "Great " + magicians[count]


def show_magicians(magicians):
    for magician in magicians:
        print(magician)


magicians = ['shaoda', 'xuanxuan', 'mrrnonsense', 'jyangjun', 'xiaoming']
make_great(magicians)
show_magicians(magicians)
