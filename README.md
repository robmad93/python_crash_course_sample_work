# Python Crash Course Sample Work
A collection of some of my more notable attempts at answering the exercises provided within the incredible resource "Python Crash Course, Edition 2" by Eric Matthes. I have provided detailed comments in all python files to explain what the code does; please read through these comments in the individual python files to understand what each file does. I have provided descriptions for what each python file does below.

## addition_calculator.py
This Python program allows users to continuously add pairs of numbers entered via the console. It catches ValueError exceptions that occur if non-numeric input is provided. The program prompts the user to enter two numbers, calculates their sum, displays the result, and then asks if the user wishes to continue adding more numbers. If the user enters 'N', the program terminates; otherwise, it continues prompting for more input.

## album_artist_generator.py
This Python script allows users to build a collection of music albums by continuously prompting for artist names, album titles, and optionally, the number of songs in each album. It uses a make_album function that returns a dictionary describing each album. The script runs in an infinite loop until the user opts to quit by entering 'q'. Each album's details are formatted and displayed as they are entered, and the entire collection is printed at the end.

## alien_colours.py
Contains Python snippets that demonstrate different scenarios based on conditions and lists:

Exercises 5-3 to 5-5: The code checks the color of an alien and awards points accordingly. If the alien is green, the player earns 5 points; if yellow, 10 points; and if red, 15 points. The points awarded are based on the color of the alien defined in alien_colour.

Exercise 5-6: This snippet determines the life stage based on the age provided. It categorizes individuals into various stages such as "Baby", "Toddler", "Kid", "Teenager", "Adult", or "Elder" depending on their age.

Exercise 5-7: Here, the script checks if a specified fruit (regardless of case) is in the list of favorite fruits (fav_fruits). If the fruit (in this case, "BANANAS") is found in the list, it prints a message indicating the user really likes that fruit. If not found, it informs the user that the fruit is not among their favorite fruits.

These snippets cover conditional statements, list operations, and basic string manipulation in Python.

## cat.py
The Python code defines a Cat class that models a cat with attributes name and age. It includes methods meow() and purr() to make the cat meow and purr respectively. An instance my_cat of the Cat class is created with the name "Tiger Tom" and age 5, followed by invoking the meow() method on my_cat, causing it to print "Tiger Tom is meowing!"

## cat_and_dog_file_reader.py
The Python code uses the os module to change the current working directory. It then attempts to open and read two files, "cats.txt" and "dogs.txt". If successful, it prints the contents of each file line by line after stripping any extra whitespace. If either file is not found (FileNotFoundError), it prints "Sorry. It appears a file is missing!"

## city_functions.py
The city_country function formats and returns a string representing a city and its associated country. It takes in city_name and country_name as required arguments, and an optional population argument which defaults to an empty string. If population is provided (not empty), the function includes it in the formatted string; otherwise, it omits population details. The returned string is capitalized using .title() to ensure consistent formatting.

## dice.py
The Python code defines a Die class that models a six-sided die. Upon initialization (__init__ method), it sets the number of sides to 6. The class includes a method roll_die(number_of_rolls) that simulates rolling the die a specified number of times (number_of_rolls). Each roll generates a random number between 1 and 6 using randint() from the random module, and prints the result in the format "Roll {number}: {result}".

## employee.py
The Employee class models an employee with attributes including first name, last name, and annual salary. It provides methods to initialize these attributes (__init__()), and to give the employee a raise (give_raise(value)), where the default raise is $5,000 if no value is specified. The class encapsulates basic employee management functionality, allowing for easy instantiation and modification of employee salary information.

Uncomment the provided lines below the class definition to test its functionality, including creating an instance of Employee, giving the employee a raise, and printing the updated annual salary. This class is suitable for scenarios where managing employee data and salary adjustments are necessary.

## fav_number_json_dump.py
The Python code prompts the user to input their favorite number. It then stores this number in a file named "favourite_number.json" using JSON format. The process involves opening the file in write mode, using the json.dump() function to serialize the fav_number into the file. Finally, it informs the user that their favorite number has been successfully saved to the specified file. This script is useful for capturing and persisting user preferences or data in a structured format like JSON, ensuring that the information can be easily retrieved and processed later.

## fav_number_json_load.py
The Python code reads a favorite number stored in a JSON file named "favourite_number.json". It opens the file in read mode and uses json.load() to deserialize the JSON data into the variable number. Finally, it prints a message confirming that it knows the user's favorite number.

## favorite_number_remembered.py
This script manages a user's favorite number using JSON. It first tries to open a file (favourite_number.json) to retrieve and print the stored favorite number. If the file doesn't exist or isn't readable (FileNotFoundError), it prompts the user to input their favorite number. The script then writes this number to the file in JSON format for future reference and confirms to the user that their favorite number has been saved.

## guest_book.py
This Python code demonstrates a simple guest book application. It maintains a guest book where users can add their names upon visiting. It first sets the working directory using the os module. If the guest book file "guest_book.txt" doesn't exist, it creates it and initializes it with a header "---Guestbook---". The user is prompted to enter their name, which is then appended to the guest book file along with a message indicating their visit. This script is useful for keeping track of visitors or interactions in a straightforward text-based format.

## guest_book_generator.py
This script manages a guest book stored in a file named "guest_book.txt". It initializes the file if it doesn't exist, prompting users to enter their name and recording it in the guest book. It handles potential IOError exceptions that may arise during file operations, ensuring robustness when writing visitor entries.

This guest book application is designed to track and acknowledge visits with simplicity and reliability, suitable for basic interaction logging in a specified directory on your system.

## guest_list.py
The Python code manages a dinner party guest list with initial invitations to David Goggins, Joe Rogan, and Jennifer Doudna. It updates the list by replacing Jennifer Doudna with Michael Collins and sends individualized invitations. Later, it expands the guest list with Lex Fridman, Nikola Tesla, and Emmanuelle Charpentier due to a bigger table, confirming the total number of guests. Finally, realizing a delay in the table's arrival, it reduces the guest list to two using pop() and eventually clears the list entirely with del.

## guest_list_generator.py
This script manages a guest list stored in a file named 'guest.txt'. It continuously prompts users to enter their names and checks if each name is already present in the list. If the name is not already included, it appends it to the file and confirms its addition. If the name is already in the list, it prompts the user to enter a different name to avoid duplicates.

## hello_admin.py
The script begins by greeting users in a predefined list of usernames. It specifically addresses the user "admin" with a tailored message, while other users receive a standard greeting. It then checks a new set of usernames against an existing list to determine availability, providing feedback on whether each username is already taken or can be used. Finally, it formats and prints a series of numbers with their respective ordinal suffixes (e.g., 1st, 2nd, 3rd) up to the ninth number, adhering to typical English ordinal conventions.

## json_load.py
This script manages JSON data stored in a file named "numbers.json". It attempts to open and read the contents of the file using json.load() to load the JSON data into the numbers variable. If the file exists and contains valid JSON data, it prints the loaded data. If the file doesn't exist (FileNotFoundError) or contains invalid JSON (json.JSONDecodeError), appropriate error messages are displayed to inform the user of the issue.

## json_test.py
This script serializes a list of numbers [2, 3, 5, 7, 11, 13] into JSON format and saves it to a file named "numbers.json". Using Python's json.dump() function, the script opens the file in write mode and writes the serialized JSON representation of the list to the file. This process effectively stores the list data in a structured format that can be easily read and processed by other programs or scripts that support JSON.

## learning_python_run.py
This script reads the file "learning_python.txt" located in a specified directory. It iterates through each line in the file, replacing occurrences of the substring "Python" with "R" using the replace() method. After replacing the text, it prints each modified line with leading and trailing whitespace removed (strip() function).

## lottery.py
This script simulates a lottery game with a predefined set of options including numbers (1-10) and letters (a-e). It defines a Lottery class that initializes with these options and provides methods to run the lottery (run_lottery()) and reset the winning selection (reset_winning_selection()).

The main loop continuously runs the lottery until the winning selection matches a predefined ticket (my_ticket), which is represented as a set of 4 chosen options (numbers or letters). It keeps track of the number of attempts made (number_of_attempts) and prints the winning selection and the number of attempts upon finding a match.

This implementation allows for the simulation of a lottery game where you can define your ticket and see how many attempts it takes to match the winning selection. It demonstrates basic usage of classes, sets, loops, and conditional statements in Python.

## make_car.py
The make_car function constructs a dictionary containing details about a car based on provided arguments. It requires mandatory parameters manufacturer and model, which specify the car's make and model. Additional details can be included using keyword arguments (**kwargs), which are captured in the dictionary kwargs. This function is useful for dynamically creating structured data representations of cars with varying details beyond just manufacturer and model.

## make_shirt.py
The make_shirt function prints a message describing a shirt being made, with default parameters for size and text. The describe_city function prints the name of a city and its associated country, defaulting to Ireland if no country is specified. The city_country function prints a formatted string of "city, country". Finally, the make_album function returns a dictionary describing a music album, including the artist name and album title, optionally including the number of songs if provided by the user in an interactive loop.

## number_loops.py
This code demonstrates several operations using Python:

First, it generates a list of cubes of numbers from 1 to 10 using a list comprehension and prints the resulting list. Then, it calculates and prints the sum of these cubes. Next, it creates a list of squares of numbers from 1 to 10 using another list comprehension and prints that list. Following this, it prints numbers from 0 to 20. Later, it creates a list containing numbers from 0 to 1,000,000 and prints the sum of these numbers. Then, it generates a list of odd numbers from 1 to 20 using a list comprehension and prints the list. Finally, it manually creates a list of multiples of 3 from 3 to 30 and prints this list.

## pizza.py
The function make_pizza is designed to summarize the details of a pizza being made. It takes two parameters: size, which indicates the size of the pizza in inches (an integer), and *toppings, which allows for a variable number of toppings to be passed to the function.

When called, the function prints a summary of the pizza being prepared, including its size in inches. It then iterates through the toppings tuple (created by the *toppings parameter) and prints each topping on a new line prefixed with a dash ("-").
 This function effectively provides a concise overview of the pizza order, specifying both the size and the toppings selected.

## pizza_toppings.py
This code interacts with the user to gather toppings for a pizza until they enter "quit". Each topping entered is displayed as added to the pizza. After the user finishes adding toppings by typing "quit", it removes an initial empty entry and prints the accumulated toppings in a formatted list.

## programming_poll.py
This script manages a programming poll by first setting the working directory and initializing a file named "programming_poll.txt" if it doesn't already exist. It then enters an infinite loop where it prompts users to input their name and their reason for liking programming. Users can exit the loop by entering 'q' in response to either prompt. Each user's name and answer are appended to the file in a structured format ("Name: [name]\nAnswer: [answer]"). This process continues until the user opts to quit by entering 'q'.

## restaurant_class.py
This code defines a Restaurant class that represents a restaurant with attributes such as restaurant_name, cuisine_type, and number_served. It includes methods to describe the restaurant, indicate if it's open, set the number of customers served, and increment that number.

There's also an IceCreamStand class that inherits from Restaurant, adding a display_flavours method to list available ice cream flavors alongside the restaurant's name and cuisine type. A section at the bottom then tests the classes and methods.

## seeing_the_world.py
This code demonstrates manipulating and displaying a list of countries I want to visit. It initially prints the list, then temporarily sorts and displays it alphabetically without altering the original order. It verifies the original order hasn't changed and proceeds to sort the list in reverse alphabetical order, printing it. The list is reversed twice to show different orders before finally sorting it permanently in alphabetical and reverse alphabetical orders using the sort() method.

## test_cities.py
This code conducts unit testing using Python's unittest framework for the city_country function from city_functions.py. It verifies two scenarios: one where the function formats city and country names without population data and another where it includes population information. Each test method uses assertions to compare the output of city_country against expected formatted strings. Running unittest.main() executes these tests, ensuring the city_country function behaves correctly across different input configurations.

## test_employee.py
This code uses Python's unittest framework to test the functionality of the Employee class defined in employee.py. It includes two test methods: one to verify the default raise amount applied to an employee's salary and another to test a custom raise amount. The setUp method initializes an instance of Employee with predefined details for use in both test methods. Running unittest.main() executes these tests, ensuring that the give_raise method of the Employee class behaves correctly when adjusting the annual salary based on specified or default raise amounts.

## users.py
The code defines two classes: User and Admin, with Admin inheriting from User. The User class manages user details such as name, age, nationality, and profession, with methods to describe the user, greet them, and manage login attempts. The Admin class extends User and introduces a Privileges class to handle administrative privileges like adding posts, deleting posts, and banning users. The show_privileges method in Privileges prints these privileges. Testing includes creating instances of User and Admin, demonstrating methods like describe_user, greet_user, increment_login_attempts, and reset_login_attempts, as well as displaying admin privileges using show_privileges.

## word_counter.py
The provided program defines a Wordfinder class that counts occurrences of a specified word in a given text file. It initializes with the word to search for (word_to_find) and the path to the text file (text_file). The find_word method reads through each line of the text file, splits lines into words, and compares each word to word_to_find, incrementing word_count for each match. The print_word_count method outputs the total count of occurrences for the word in the text file when called.
