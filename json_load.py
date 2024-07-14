import json

# Define the filename where JSON data is stored
filename = "numbers.json"

try:
    # Attempt to open and read the contents of the JSON file
    with open(filename) as f:
        numbers = json.load(f)  # Load JSON data from the file into the 'numbers' variable
        print(numbers)  # Print the loaded JSON data
except FileNotFoundError:
    # Handle the case where the file doesn't exist
    print(f"Error: The file '{filename}' does not exist.")
except json.JSONDecodeError:
    # Handle the case where the file exists but does not contain valid JSON data
    print(f"Error: '{filename}' does not contain valid JSON data or is empty.")