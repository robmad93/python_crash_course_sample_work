import os

# Change the current working directory to the specified path
# Ensure this path matches the actual location of your files.
os.chdir("Desktop/python_work")

try:
    # Attempt to open and read the contents of the "cats.txt" file.
    with open("cats.txt", "r") as cats:
        print("\nThe following cats are present: ")
        # Print each line in the file after stripping any extra whitespace.
        for line in cats:
            print(line.strip())
    
    # Attempt to open and read the contents of the "dogs.txt" file.
    with open("dogs.txt", "r") as dogs:
        print("\nThe following dogs are present: ")
        # Print each line in the file after stripping any extra whitespace.
        for line in dogs:
            print(line.strip())

# Catch the FileNotFoundError if either file does not exist.
except FileNotFoundError:
    print("Sorry. It appears a file is missing!")