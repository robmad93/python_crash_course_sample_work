# Create and test instances of User and Admin classes.

class User:
    """Creating a class that describes a user."""
    def __init__(self, first_name, last_name, age, nationality, profession):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nationality = nationality
        self.profession = profession
        self.login_attempts = 0

    def describe_user(self):
        """Summarizes user's details."""
        print(
            f"Full name: {self.first_name} {self.last_name},\n Age: {self.age}, \n Nationality: {self.nationality}, \n Profession: {self.profession}, \n Login attempts: {self.login_attempts}"
        )

    def greet_user(self):
        """Prints a personalized greeting."""
        print(f"Greetings, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        """Incremements the number of login attempts by one."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset number of login attempts."""
        self.login_attempts = 0

# Creating a subclass called Admin that inherits from the User superclass.

class Admin(User):
    def __init__(self, first_name, last_name, age, nationality, profession):
        super().__init__(first_name, last_name, age, nationality, profession)
        self.privileges = Privileges()


"""Creating a separate class for privileges."""


class Privileges:
    def __init__(self):
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            "can add member",
            "can promote post",
            "can assign roles",
        ]

    def show_privileges(self):
        """Prints list of admin privileges."""
        print("The admin has the following privileges: ")
        for privilege in self.privileges:
            print(f"- {privilege}")


# Testing the above classes and methods. Uncomment the below code to run.

# user_1 = User("Jeff", "Bezos", 60, "American", "Businessman")
# user_1.describe_user()
# user_1.greet_user()

# user_2 = User("Joe", "Biden", 81, "American", "President")
# user_2.describe_user()
# user_2.greet_user()

# for i in range(5):
#     user_2.increment_login_attempts()

# user_2.describe_user()

# user_2.reset_login_attempts()
# user_2.describe_user()

# admin = Admin("Robert", "Madigan", 31, "Irish", "Programmer/Editor")
# admin.privileges.show_privileges()
