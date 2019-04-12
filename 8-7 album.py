# 8-7. Album: Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.
# Add an optional parameter to make_album() that allows you to store the
# number of tracks on an album. If the calling line includes a value for the number
# of tracks, add that value to the album’s dictionary. Make at least one new
# function call that includes the number of tracks on an album.

def album(artist_name, album_title, track_number=''):
	album_info = {
		'artist': artist_name,
		'title': album_title,
	}
	if track_number:
		album_info['track'] = track_number
	return album_info
	
album_info = album("shaoda","emmmm")

for key, value in album_info.items():
	print(key.title() + ": " + value.title())

album_info = album("shaoda","emmmm","10")

for key, value in album_info.items():
	print(key.title() + ": " + value.title())
