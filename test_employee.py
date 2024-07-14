import unittest
from employee import Employee # Assuming 'Employee' class is defined in 'employee.py'


class TestEmployee(unittest.TestCase):
    """Tests for the Employee class."""

    def setUp(self):
        """Create employee details for use in all test methods."""
        self.employee_1 = Employee("John", "McGee")

    def test_give_default_raise(self):
        """Test default raise amount."""
        self.employee_1.give_raise()
        self.assertEqual(self.employee_1.annual_salary, 5000)

    def test_give_custom_raise(self):
        """Test custom raise amount."""
        self.employee_1.give_raise(6000)
        self.assertEqual(self.employee_1.annual_salary, 6000)


if __name__ == "__main__":
    unittest.main()
