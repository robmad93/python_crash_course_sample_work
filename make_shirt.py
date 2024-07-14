def make_shirt(size="Large", text="I love Python"):
    """Prints a message describing the shirt being made."""
    print(f"Making a shirt of size {size} with the following text: '{text}'")

# Example usage:
make_shirt()

def describe_city(city, country="Ireland"):
    """Prints the name of a city and its country."""
    print(f"{city} is in {country}")

# Example usage:
describe_city("Dublin")

def city_country(city, country):
    """Prints a formatted string of 'city, country'."""
    print(f"{city}, {country}")

# Example usage:
city_country("Paris", "France")

def make_album(name, title, songs=None):
    """
    Returns a dictionary describing a music album.
    
    Args:
    - name: Artist name (str)
    - title: Album title (str)
    - songs: Number of songs in the album (int), optional
    
    Returns:
    - Dictionary with artist name and album title. If songs is provided, includes number of songs.
    """
    album = {'Artist name': name.title(), 'Album title': title.title()}
    if songs:
        album['Number_of_songs'] = songs
    return album

# Interactive album creation loop
while True:
    print("Please enter an artist name")
    print("(enter 'q' at any time to quit)")
    artist_name = input("Artist's name: ")
    if artist_name == 'q':
        break
    print("Please enter an album name")
    print("(enter 'q' at any time to quit)")
    album_name = input("Album name: ")
    if album_name == 'q':
        break

    # Create and display the album dictionary
    make_album(artist_name, album_name)