# Python crash course, Exercises 3-4 to 3-7.
# I'm planning a dinner party! Let's invite three guests!
guests = ['David Goggins', 'Joe Rogan', 'Jennifer Doudna']
print(f"Welcome to my dinner party, {', '.join(guests)}")

# Albert Einstein can't make it, what a shame!
print(f"{''.join(guests[2])} can't make it")

# I'll invite the Irish freedom fighter, Michael Collins.
guests[2] = "Michael Collins"
print(guests)

# I'll send separate invites this time.
message_1 = f"\nYou are invited, {''.join(guests[0])}"
message_2 = f"\nLooking forward to catching up, {''.join(guests[1])}"
message_3 = f"\nCan't wait to chat, {''.join(guests[2])}"
print(message_1, message_2, message_3)

# Oh good, I just found a bigger dinner table. Let's invite more guests!
print(f"{', '.join(guests)}, good news! I found a bigger dinner table")

# Adding more guests
# Adding one new guest to the beginning of my list using the insert() method.
guests.insert(0, "Lex Fridman")
# Adding one new guest to the middle of my list using the insert() method.
guests.insert(2, "Nikola Tesla")
# # Adding one new guest to the end of my list using the append() method.
guests.append("Emmanuelle Charpentier")

print(f"Number of guests: {len(guests)}")

# Let's send a new set of invites out.
for i in guests:
	print(f"\nYou are invisted to my dinner part, {i}")

# Oh no, the dinner table won't arrive in time! I guess I'll only have room for two guests...
print("\nI can only invite two guests")

# Using pop to remove guests from my list.
for i in range(4):
	guests.pop()

# Sending a message to the final two guests.
print(f"{' and '.join(guests)}, you guys are still invited!")

# Actually, maybe I need to start from scratch with an empty list...
del guests[0:2]
print(guests)