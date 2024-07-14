import json

# Define the name of the file where the favorite number is stored.
filename = "favourite_number.json"

try:
    # Try to open the file in read mode and load the favorite number using JSON format.
    with open(filename) as f:
        number = json.load(f)
        # Print the favorite number if the file exists and is readable.
        print(f"I know your favorite number! It's {number}.")
except FileNotFoundError:
    # If the file is not found, prompt the user for their favorite number.
    fav_number = input("What's your favorite number?: ")
    # Open the file in write mode and store the favorite number using JSON format.
    with open(filename, "w") as f:
        json.dump(fav_number, f)
        # Inform the user that their favorite number has been saved.
        print("I'll remember your favorite number next time!")
