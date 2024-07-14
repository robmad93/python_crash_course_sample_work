prompt = ""            # Initialize the prompt variable
added_toppings = []    # Initialize an empty list to store toppings

# Loop to gather pizza toppings until user enters "quit"
while prompt != "quit":
    print(f"{prompt} has been added to your pizza")
    added_toppings.append(prompt)    # Add the current topping to the list
    prompt = input("Please add a topping: ")    # Prompt user for next topping
    print()
    
    if prompt.lower() == "quit":    # Check if user wants to quit (case insensitive)
        break

added_toppings.remove("")    # Remove empty string added as the first entry

# Print the list of added toppings
print("Your pizza toppings:", ", ".join(added_toppings))