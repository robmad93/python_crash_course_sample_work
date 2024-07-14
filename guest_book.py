# Import the os module to handle directory operations
import os

# Set the working directory where the file will be located
os.chdir("Desktop/python_work")  # Change directory as required

# Define the name of the guest book file
file_name = "guest_book.txt"

# Check if the file already exists; if not, create and initialize it
if not os.path.exists(file_name):
    with open(file_name, "w") as file_object:
        file_object.write("---Guestbook---\n")

# Prompt the user to enter their name
name = input("Please enter your name: ")
print(f"Greetings, {name}!")

# Append the user's name to the guest book file
with open(file_name, "a") as file_object:
    file_object.write(name + " has visited.\n")
