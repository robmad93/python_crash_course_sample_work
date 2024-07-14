# Lottery generator and attempt counter.

from random import choice


class Lottery:
    def __init__(self):
        """Define the pool of options for the lottery"""
        self.options = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e")
        self.winning_selection = []  # Initialize an empty list to store the winning selection

    def run_lottery(self):
        """Run the lottery to generate a winning selection of 4 unique options"""
        while len(self.winning_selection) < 4:
            selection = choice(self.options)  # Randomly pick an option from self.options
            if selection in self.winning_selection:
                continue  # If the option is already in winning_selection, skip and pick again
            else:
                self.winning_selection.append(selection)  # Add the unique option to winning_selection
        print(self.winning_selection)  # Print the winning selection after it's generated

    def reset_winning_selection(self):
        """Reset the winning_selection list to empty"""
        self.winning_selection = []

# Create an instance of the Lottery class
lottery = Lottery()

# Define your ticket with 4 chosen options (numbers or letters)
my_ticket = {3, "d", "e", 1}

number_of_attempts = 0  # Initialize a counter for the number of attempts

# Loop to run the lottery until the winning selection matches your ticket
while True:
    lottery.run_lottery()  # Run the lottery to generate a new winning selection
    number_of_attempts += 1  # Increment the attempt counter

    # Check if the current winning selection matches your ticket
    if set(lottery.winning_selection) == my_ticket:
        print(f"We have a winner! Number of tries: {number_of_attempts}")
        break  # Exit the loop if there's a match

    lottery.reset_winning_selection()  # Reset the winning selection for the next attempt