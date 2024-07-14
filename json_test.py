import json

# Define a list of numbers to be stored in a JSON file
numbers = [2, 3, 5, 7, 11, 13]

# Specify the filename where JSON data will be saved
filename = "numbers.json"

# Open the file in write mode and write the list of numbers to it as JSON
with open(filename, "w") as f:
    json.dump(numbers, f)  # Serialize 'numbers' list into JSON format and write to file