from nested_data import albums

# print(albums)
SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

while True:
    print("Please choose your album (invalid choice exits):")
    for index, (title, artist, year, songs) in enumerate(albums):
        # print("{}: {}, {}, {}, {}"
        #       .format(index + 1, title, artist, year, songs))
        print("{}: {}"
              .format(index + 1, title))
    # print("*" * 50)

    # for index, value in enumerate(albums):
    #     title, artist, year, songs = value
    #     print(index, title, artist, year, songs)

    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LIST_INDEX]
    else:
        break

    # print(albums[choice - 1])
    # print(songs_list)
    # print()

    print("Please choose your songs:")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song))

    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
    # else:
    #     break
        print("Playing {}".format(title))

    print("=" * 40)
