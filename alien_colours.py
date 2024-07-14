# Python crash course, exercises 5-3 to 5-7.

# Exercises 5-3 to 5-5. Checking the color of the alien and awarding points accordingly.
alien_colour = 'red'

if alien_colour == 'green':
	print("Player has earned 5 points")
elif alien_colour == 'yellow':
		print("Player has earned 10 points")
elif alien_colour == 'red':
	print("Player has earned 15 points")

# Exercise 5-6: Determining life stage based on age.
age = 65

if age < 2:
	print("Baby")
elif age >= 2 and age < 4:
	print("Toddler")
elif age >= 4 and age < 13:
	print("Kid")
elif age >= 13 and age < 20:
	print("Teenager")
elif age >= 20 and age < 65:
	print("Adult")
elif age >= 65:
	print("Elder")

# Exercise 5-7: Checking if a specific fruit is in the list of favorite fruits.
fav_fruits = ["bananas", "raspberries", "strawberries", "blueberries", "oranges"]

# Check if a particular fruit (case insensitive) is in the list of favorite fruits
fruit = "BANANAS"
if fruit.lower() in fav_fruits:
	print(f"You really like {fruit.lower()}")
# Handle the case where the fruit is not in the list of favorite fruits
else:
	print(f"{fruit.title()} aren't among your favourite fruits")
