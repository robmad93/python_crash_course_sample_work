"""
This script manages a guest list stored in a file named 'guest.txt'. 
It prompts users to enter their names and checks if each name is already 
in the list. If a name is not already present, it appends it to the file 
and confirms its addition. If the name is already in the list, it prompts 
the user to enter a different name.
"""
import os

# Define the path to the guest.txt file.
filename = "Desktop/python_work/guest.txt"

# Check if the file already exists; if not, create and initialize it.
if not os.path.exists(filename):
    with open(filename, "w") as file_object:
        file_object.write("---Guest List---\n")

# Continuously prompt the user to enter a guest name.
while True:
    guest = input("Please enter your name: ")

    # Open the file in read mode to check if the name already exists.
    with open(filename, "r") as file_object:
        guests = file_object.readlines()

    # Check if the entered name is already in the file.
    if any(guest.strip() == line.strip() for line in guests):
        print("This name has already been entered. Please try again.")
    else:
        # If the name is not in the file, open it in append mode to add the new name.
        with open(filename, "a") as file_object:
            file_object.write("\n" + guest.strip())
        print(f"Guest name '{guest}' has been added.")
        break