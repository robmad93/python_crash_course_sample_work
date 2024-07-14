# Simple program for adding numbers and catching ValueErrors when they arise.
while True:
    try:
        # Prompt the user to enter the first number and convert it to an integer
        number_1 = int(input("Please enter a number: "))
        
        # Prompt the user to enter the second number and convert it to an integer
        number_2 = int(input("Please enter another number: "))
        
        # Calculate the sum of the two numbers
        answer = number_1 + number_2
        
        # Display the result of the addition
        print(f"{number_1} + {number_2} = {answer}")
        
        # Ask the user if they want to continue or not
        prompt = input("Do you wish to continue? Y/N: ")
        
        # If the user inputs 'N', break the loop and end the program
        if prompt == "N":
            break
    
    # Handle the case where the user inputs a non-numeric value
    except ValueError:
        print("Sorry. I cannot add words. Please provide numbers.")
