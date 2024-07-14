class Restaurant:
    """A class to represent a restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of the restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print a description of the restaurant."""
        print(f"{self.restaurant_name} specializes in {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Print a message indicating the restaurant is open."""
        print(f"{self.restaurant_name} is open for business!")

    def set_number_served(self, number_served):
        """Set the number of customers served."""
        self.number_served = number_served

    def increment_number_served(self, number_served):
        """Increment the number of customers served."""
        self.number_served += number_served


class IceCreamStand(Restaurant):
    """A subclass representing an ice cream stand, inheriting from Restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of the parent class and flavors."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ["vanilla", "chocolate", "banana", "strawberry"]

    def display_flavours(self):
        """Print all available ice cream flavors."""
        print("The following flavors are available:")
        for flavour in self.flavours:
            print(f"- {flavour}")


# Testing the above classes and methods

# Creating an instance of IceCreamStand and testing display_flavours method
ice_cream_stand = IceCreamStand("Gelato", "Dessert")
ice_cream_stand.display_flavours()

# Creating instances of Restaurant and testing methods
my_restaurant = Restaurant("Madigan's Pub", "Pub")
my_restaurant.open_restaurant()

italian_restaurant = Restaurant("Luigi's", "Italian")
french_restaurant = Restaurant("La Mer", "French")
japanese_restaurant = Restaurant("Osaka", "Japanese")

italian_restaurant.describe_restaurant()
french_restaurant.describe_restaurant()
japanese_restaurant.describe_restaurant()

# Creating another instance of Restaurant and testing number_served methods
generic_restaurant = Restaurant("O' Shea's", "Irish")
generic_restaurant.set_number_served(5)
print(
    f"{generic_restaurant.restaurant_name} has served {generic_restaurant.number_served} customers."
)
generic_restaurant.increment_number_served(10)
print(
    f"{generic_restaurant.restaurant_name} has now served {generic_restaurant.number_served} customers."
)