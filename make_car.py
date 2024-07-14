def make_car(manufacturer, model, **kwargs):
    """
    Builds a dictionary containing information about a car.

    Args:
    manufacturer (str): The car's manufacturer.
    model (str): The car's model.
    **kwargs (dict): Additional keyword arguments for car details.

    Returns:
    dict: Dictionary containing car information.
    """
    kwargs["manufacturer"] = manufacturer
    kwargs["model"] = model
    return kwargs


car_1 = make_car("Honda", "Civic", engine="2 L", colour="black")
print(car_1)