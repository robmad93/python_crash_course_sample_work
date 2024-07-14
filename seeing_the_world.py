# Python crash course, exercise 3-8.
# List of my top five countries I'd like to visit.
locations = ["Canada", "Australia", "Japan", "Columbia", "India"]

print(locations)

# Temporarily sorting the list in alphabetical order.
print(sorted(locations))

# Verifying that my list is still in its original order.
print(locations)

# In reverse alphabetical order.
print(sorted(locations, reverse = True))

locations.reverse()
print(locations)

# Return to original order.
locations.reverse()
print(locations)

# Sort in alphabetical order (permanently) using sort().
locations.sort()
print(locations)

# Now in reverse alphabetical order.
locations.sort(reverse = True)
print(locations)