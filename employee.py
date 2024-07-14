class Employee:
    """A class to represent an employee."""

    def __init__(self, first_name, last_name, annual_salary=0):
        """
        Initialize the employee with first name, last name, and annual salary.
        
        :param first_name: str, the first name of the employee
        :param last_name: str, the last name of the employee
        :param annual_salary: int, the annual salary of the employee (default is 0)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, value=5000):
        """
        Increase the employee's annual salary by a specified amount.
        
        :param value: int, the amount to increase the salary by (default is $5,000)
        :return: int, the new annual salary
        """
        self.annual_salary += value
        return self.annual_salary

# Uncomment the lines below to test the Employee class

# Create an instance of the Employee class
# test = Employee("John", "McGee")

# Give the employee a raise (default raise is $5,000)
# test.give_raise()

# Print the employee's new annual salary
# print(test.annual_salary)