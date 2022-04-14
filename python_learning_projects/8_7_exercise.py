album_name_def = input("what's the album's name ? ")
artist_name_def = input("what's the artist's name ? ")
track_numbers_def = input("what's the number of tracks in the album ? ")

def album_maker(album_name,artist_name,track_numbers=""):
    """this makes an info sheet for an album"""

    if track_numbers_def:
        album_info = {
        "album_name":album_name,
        "artist_name":artist_name,
        "track_numbers":track_numbers
        }
    else:
        album_info = {
        "album_name":album_name,
        "artist_name":artist_name
        }

    return(album_info)

album_info_sheet = album_maker(album_name_def,artist_name_def,track_numbers_def)
for field,information in album_info_sheet.items():
    print(field + ":\n\t" + information)
