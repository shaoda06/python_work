# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of
# three names to use as keys in the dictionary, and store one to three
# favorite places for each person. To make this exercise a bit more
# interesting, ask some friends to name a few of their favorite places. Loop
# through the dictionary, and print each person’s name and their favorite
# places.

favorite_places = {
    'shaoda': ['shanghai', 'sichuan', 'chongqing'],
    'mrrnonsense': ['mcallen', 'los angeles', 'new york'],
    'jyangjun': ['beijing', 'tianjin', 'beidaihe'],
}

for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favorite places are: ")
    for place in places:
        print("\t" + place.title())
