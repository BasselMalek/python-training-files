#this is another version of 8_7_exercise.py to test another program body
def album_maker(album_name_def,artist_name_def,track_numbers_def=""):
    """album sheet maker"""
    if track_numbers_def:
        album_info={
        "album_name":album_name_def,
        "artist_name":artist_name_def,
        "track_numbers":track_numbers_def
        }
    else:
        album_info={
        "album_name":album_name_def,
        "artist_name":artist_name_def
        }
    return album_info

while True:
    album_name = input("what's the album's name ? ")
    if (album_name=="end"):
        break
    artist_name = input("what's the artits's name ? ")
    if (artist_name=="end"):
        break
    track_numbers = input("how many tracks are there in the album ? ")
    if (track_numbers=="end"):
        break

    info_dic = album_maker(album_name,artist_name,track_numbers)
    for info_field,info in info_dic.items():
        print(info_field.title() + ":\n\t" + info.title())
    confirmation = input("do you want to create another sheet ? ")
    if (confirmation=="yes"):
        continue
    elif (confirmation=="no"):
        print("Thank you for using Album Sheet maker")
        break
