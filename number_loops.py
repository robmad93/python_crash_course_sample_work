# List comprehension to create a list of cubes of numbers from 1 to 10
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)

# Calculate the sum of all cubes
print(sum(cubes))

# List comprehension to create a list of squares of numbers from 1 to 10
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# Print numbers from 0 to 20 (inclusive)
# Python crash course, exercise 4-3 to 4-9.
for i in range(21):
    print(i)

# Create a list of numbers from 0 to 1,000,000
million = [i for i in range(1000001)]
print(sum(million))

# Create a list of odd numbers from 1 to 20
odd = [i for i in range(1, 21, 2)]
print(odd)

# Create a list of multiples of 3 from 3 to 30
mult_of_3 = []
for i in range(3, 31):
    if i * 3 <= 30:
        mult_of_3.append(i * 3)
    else:
        break
print(mult_of_3)