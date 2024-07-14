import os

# Set the working directory where the file will be located
os.chdir("Desktop/python_work")

# Define the name of the guest book file
file_name = "guest_book.txt"

# Check if the file already exists; if not, create and initialize it
if not os.path.exists(file_name):
    with open(file_name, "w") as file_object:
        file_object.write("---Guestbook---\n")

# Prompt the user to enter their name
name = input("Please enter your name: ")
print(f"Greetings, {name}!")

try:
    # Open the guest book file in append mode and write the visitor's name
    with open(file_name, "a") as file_object:
        file_object.write(f"{name} has visited.\n")
    print("Your visit has been recorded in the guest book.")
except IOError:
    # Handle IOError in case there's an issue opening or writing to the file
    print(f"Error: Could not write to file {file_name}. Please check file permissions or try again later.")