import unittest

from city_functions import city_country


class CityCountryTestCase(unittest.TestCase):
    """Tests for city_functions.py"""

    def test_city_country(self):
        """Test case for city_country function without population."""
        formatted = city_country("santiago", "chile")
        self.assertEqual(formatted, "Santiago, Chile")

    def test_city_country_population(self):
        """Test case for city_country function with population."""
        formatted = city_country("santiago", "chile", 5000000)
        self.assertEqual(formatted, "Santiago, Chile, Population: 5000000")


if __name__ == "__main__":
    unittest.main()
