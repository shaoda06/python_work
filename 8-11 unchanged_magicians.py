# 8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the
# function make_great() with a copy of the list of magicians’ names. Because the
# original list will be unchanged, return the new list and store it in a separate list.
# Call show_magicians() with each list to show that you have one list of the original
# names and one list with the Great added to each magician’s name.


def make_great(magicians):
    great_magicians = []
    for count in range(0, len(magicians)):
        great_magicians.append("Great " + magicians[count])
    return great_magicians


def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())


magicians = ['shaoda', 'xuanxuan', 'mrrnonsense', 'jyangjun', 'xiaoming']
great_magicians = make_great(magicians[:])
show_magicians(magicians)
show_magicians(great_magicians)
