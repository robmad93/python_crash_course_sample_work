class Cat:
    """A simple cat model."""

    def __init__(self, name, age):
        """
        Initialize the cat with a name and age.
        
        :param name: str, the name of the cat
        :param age: int, the age of the cat.
        """
        self.name = name
        self.age = age

    def meow(self):
        """Invoke the cat to meow."""
        print(f"{self.name} is meowing!")

    def purr(self):
        """Invoke the cat to purr."""
        print(f"{self.name} is now purring...")

# Create an instance of the Cat class
my_cat = Cat("Tiger Tom", 5)

# Call the meow method on the Cat instance
my_cat.meow()
