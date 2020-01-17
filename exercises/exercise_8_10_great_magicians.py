# 8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
# Write a function called make_great() that modifies the list of magicians by
# adding the phrase the Great to each magician’s name. Call show_magicians()
# to see that the list has actually been modified.


def show_magicians(magician_names):
    for name in magician_names:
        print(name.title())


def make_great(magician_names):
    for index in range(0, len(magician_names)):
        magician_names[index] = "Great " + magician_names[index]


magicians = ['shaoda', 'mrrnonsense', 'icehanba', 'jyangjun', 'xiaoming']
make_great(magicians)
show_magicians(magicians)
