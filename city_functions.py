def city_country(city_name, country_name, population=""):
    """
    Format and return a string representing a city and its country.

    Args:
    city_name (str): The name of the city.
    country_name (str): The name of the country.
    population (int, optional): The population of the city. Defaults to "".

    Returns:
    str: Formatted string representing city, country, and optionally population.
    """
    if population:
        combined = f"{city_name}, {country_name}, Population: {population}"
    else:
        combined = f"{city_name}, {country_name}"
    return combined.title()


# Example usage:
# test = city_country("dublin", "ireland", 5000000)
# print(test)