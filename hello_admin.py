# Exercise 5-8 and 5-9: Greeting users based on their username
usernames = ["admin", "yeetus", "penny", "smoke", "angus"]

if usernames:
    for username in usernames:
        if username == "admin":
            print(f"Hello {username}, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!")

# Exercise 5-10: Checking available usernames
current_users = ["sparky", "dunes", "frost", "edge", "simba", "edmond", "lila"]
new_users = ["big_smoke", "simba", "asterix", "golum", "frost"]

for name in new_users:
    if name.lower() in [user.lower() for user in current_users]:
        print(f"{name.lower()} is already in use. Please enter a new username.")
    else:
        print(f"{name.lower()} is available.")

# Exercise 5-11: Printing ordinal numbers
numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print(f"{number}st\n")
    elif number == 2:
        print(f"{number}nd\n")
    elif number == 3:
        print(f"{number}rd\n")
    else:
        print(f"{number}th\n")