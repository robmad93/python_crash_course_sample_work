def make_album(name, title, songs=None):
    """Return a dictionary describing a music album."""
    album = {"Artist name": name.title(), "Album title": title.title()}
    if songs:
        album["Number_of_songs"] = songs
    return album

# Initialize the collection list outside the loop.
collection = []

# Start an infinite loop to repeatedly ask for user input
while True:
    # Prompt the user to enter an artist name
    print("Please enter an artist name")
    print("(enter 'q' at any time to quit)")
    artist_name = input("Artist's name: ")
    
    # Check if the user wants to quit
    if artist_name == "q":
        break
    
    # Prompt the user to enter an album name
    print("Please enter an album name")
    print("(enter 'q' at any time to quit)")
    album_title = input("Album name: ")
    
    # Check if the user wants to quit
    if album_title == "q":
        break
    
    # Prompt the user to enter the number of songs (optional)
    print("Please enter the number of songs (Optional): ")
    print("(enter 'q' at any time to quit)")
    number_of_songs = input("Number of songs: ")
    
    # Check if the user wants to quit
    if number_of_songs == "q":
        break
    
    # Check if the input for number of songs is alphabetic
    elif number_of_songs.isalpha():
        print("A letter cannot be entered!")
        break
    
    # Check if the input for number of songs is out of range
    elif number_of_songs and int(number_of_songs) <= 0:
        print("Number out of range!")
        break
    
    # If no number is provided, set to None
    elif number_of_songs == "":
        number_of_songs = None

    # Create the album dictionary using the make_album function
    formatted = make_album(artist_name, album_title, number_of_songs)
    
    # Print the entered album details
    print(f"You have entered: {formatted}")
    
    # Add the formatted album dictionary to the collection list
    collection.append(formatted)

# Print the entire collection of albums
print("Your collection:")
for album in collection:
    print(album)
