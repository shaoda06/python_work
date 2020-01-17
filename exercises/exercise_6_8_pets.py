# 6-8. Pets: Make several dictionaries, where the name of each dictionary is
# the name of a pet. In each dictionary, include the kind of animal and the
# owner’s name. Store these dictionaries in a list called pets. Next,
# loop through your list and as you do print everything you know about each
# pet.

wang = {
    'kind': 'dog',
    'owner': 'shaoda',
}
meow = {
    'kind': 'cat',
    'owner': 'mrrnonsense',
}
emmm = {
    'kind': 'fish',
    'owner': 'lilmrrnonsense',
}

pets = [wang, meow, emmm]
for pet in pets:
    print(pet['owner'] + " owns a " + pet['kind'] + ".\n")
