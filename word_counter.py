# Program for counting how many times a given word is mentioned in a given text file.

import os

os.chdir("Desktop/python_work")  # Change to fit current working directory


class Wordfinder:
    """Initialize variables for self, the word to find, and the text file of interest, setting the original word count
    to 0."""

    def __init__(self, word_to_find, text_file):
        self.word_to_find = word_to_find
        self.text_file = text_file
        self.word_count = 0

    def find_word(self):
        """Reads through the file line by line to count the number of appearances of the word."""
        with open(
            self.text_file, "r", encoding="utf-8"
        ) as book:  # Change to whatever text file you wish to assess
            for line in book:
                words = line.split()
                for word in words:
                    if word.lower() == self.word_to_find:
                        self.word_count += 1

    def print_word_count(self):
        """Prints a message stating how many times the word appears in the text."""
        print(
            f"This text contains {self.word_count} occurrences of the word '{self.word_to_find}'"
        )
