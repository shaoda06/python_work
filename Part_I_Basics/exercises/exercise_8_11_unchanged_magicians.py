# 8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call
# the function make_great() with a copy of the list of magicians’ names.
# Because the original list will be unchanged, return the new list and store
# it in a separate list. Call show_magicians() with each list to show that
# you have one list of the original names and one list with the Great added
# to each magician’s name.


def show_magicians(magician_names):
    for name in magician_names:
        print(name.title())


def make_great(magician_names):
    for index in range(0, len(magician_names)):
        magician_names[index] = "Great " + magician_names[index]
    return magician_names


magicians = ['shaoda', 'mrrnonsense', 'icehanba', 'jyangjun', 'xiaoming']
great_magician = make_great(magicians[:])
show_magicians(magicians)
show_magicians(great_magician)
