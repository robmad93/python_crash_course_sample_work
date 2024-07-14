# Set working directory
import os

os.chdir("Desktop/python_work")  # Change directory as required

file_name = "programming_poll.txt"

# Check if the file already exists; if not, create and initialize it
if not os.path.exists(file_name):
    with open(file_name, "w") as file_object:
        file_object.write("---Programming Poll---\n")

# Infinite loop to gather user input until 'q' is entered
while True:
    name = input("Please enter your name: ")
    print("Enter 'q' to quit")
    if name == "q":
        break
    
    answer = input("Why do you like programming?: ")
    print("Enter 'q' to quit")
    if answer == "q":
        break
    
    # Append user's name and answer to the file
    with open(file_name, "a") as file_object:
        file_object.write(f"Name: {name}\nAnswer: {answer}\n")