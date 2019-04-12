# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.


def album(artist_name, album_title, track_number=''):
    album_info = {
        'artist': artist_name,
        'title': album_title,
    }
    if track_number:
        album_info['track'] = track_number
    return album_info


while True:
    print("Enter 'quit' to finish.")
    artist_name = input("Please enter artist name: ")

    if artist_name != 'quit':
        album_title = input("Please enter album title: ")
    else:
        break

    if album_title != 'quit':
        track_number = input("Please enter track number: ")
    else:
        break

    if track_number != 'quit':
        album_info = album(artist_name, album_title, track_number)
    else:
        break

    for key, value in album_info.items():
        print(key.title() + ": " + value.title())
