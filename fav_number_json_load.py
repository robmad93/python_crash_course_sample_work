import json

# Define the name of the file where the favorite number is stored
filename = "favourite_number.json"

# Open the file in read mode and load the favorite number using JSON format
with open(filename) as f:
    number = json.load(f)
    # Print the favorite number
    print(f"I know your favorite number! It's {number}.")
