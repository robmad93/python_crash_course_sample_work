# Open the file "learning_python.txt" located in the specified directory.
with open("Desktop/python_work/learning_python.txt") as file_object:
    # Iterate over each line in the file.
    for line in file_object:
        # Replace occurrences of "Python" with "R" in the current line.
        line = line.replace("Python", "R")
        # Print the modified line with leading and trailing whitespace removed.
        print(line.strip())