import json

# Prompt the user for their favorite number
fav_number = input("What's your favorite number?: ")

# Define the name of the file where the favorite number will be stored
file_name = "favourite_number.json"

# Open the file in write mode and store the favorite number using JSON format
with open(file_name, "w") as f:
    json.dump(fav_number, f)

# Inform the user that their favorite number has been saved
print(f"Your favorite number, {fav_number}, has been saved to {file_name}.")