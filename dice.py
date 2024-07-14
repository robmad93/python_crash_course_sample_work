from random import randint


class Die:
    """A class representing a six-sided die."""

    def __init__(self):
        """Initialize the die with six sides."""
        self.sides = 6

    def roll_die(self, number_of_rolls):
        """
        Roll the die a specified number of times and print the result of each roll.

        :param number_of_rolls: int, the number of times to roll the die
        """
        # Loop through the number of rolls
        for i in range(int(number_of_rolls)):
            # Generate a random number between 1 and the number of sides on the die
            roll = randint(1, self.sides)
            # Print the result of the roll
            print(f"Roll {i + 1}: {roll}")

# Create an instance of the Die class
round_1 = Die()

# Roll the die 10 times and print the results
round_1.roll_die(10)