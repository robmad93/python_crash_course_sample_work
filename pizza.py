def make_pizza(size, *toppings):
    """
    Summarize the pizza we are about to make.
    
    Parameters:
    - size: int, size of the pizza in inches
    - *toppings: variable length argument list of toppings to be added to the pizza
    """
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")