# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have
# that information, call make_album() with the user’s input and print the
# dictionary that’s created. Be sure to include a quit value in the while loop.


def make_album(artist_name, album_title, tracks_number="unknown"):
    album = {
        "artist name": artist_name,
        "album title": album_title,
        "number of tracks": tracks_number
    }
    return album


while True:
    print("Enter 'quit' anytime to finish.")

    artist_name = input("Please enter artist name: ")
    if artist_name == 'quit':
        break
    else:
        album_title = input("Please enter album title: ")

    if album_title == 'quit':
        break
    else:
        track_number = input("Please enter track number: ")

    if track_number == 'quit':
        break
    else:
        album = make_album(artist_name, album_title, track_number)

    for key, value in album.items():
        print(key.title() + ": " + value.title())
