# 6-11. Cities: Make a dictionary called cities. Use the names of three
# cities as keys in your dictionary. Create a dictionary of information about
# each city and include the country that the city is in, its approximate
# population, and one fact about that city. The keys for each city’s
# dictionary should be something like country, population, and fact. Print
# the name of each city and all of the information you have stored about it.

cities = {
    'mcallen': {
        'country': 'united states',
        'population': 1000,
    },
    'tianjin': {
        'country': 'china',
        'population': 2000,
    },
    'beijing': {
        'country': 'china',
        'population': 3000,
    },
}
# mcallen is a 1000 population city in united states
for name, information in cities.items():
    print(
        name.title() + " is a " + str(information['population']) + " city in " +
        information['country'].title() + ".")
