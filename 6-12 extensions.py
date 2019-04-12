# 6-12. Extensions: We’re now working with examples that are complex enough
# that they can be extended in any number of ways. Use one of the example programs
# from this chapter, and extend it by adding new keys and values, changing
# the context of the program or improving the formatting of the output.

users = {
	'mrrnonsense': {
		'first': 'shaoda',
		'last': 'liu',
		'location': 'mcallen',
		},
	'jyangjun': {
		'first': 'ming',
		'last': 'yang',
		'location': 'beijing',
		},
	'gold250sam': {
		'first': 'yuanchen',
		'last': 'zhao',
		'location': 'tianjin',
		}
	}

for username, info in users.items():
	print("\nHello " + info['first'].title() + " " + info['last'].title() + "!")
	print("Your username is: " + username)
	print("Your location is: " + info['location'].title())
