import random

# Get user to input how many random numbers they want
count = int(input("How many random numbers do you want?"))

# Generate this many random numbers
numbers = [random.randint(1, 100) for _ in range(count)]

# Write the random numbers to a file named random.txt, one number per line
with open("random.txt", "w") as outfile:
    for number in numbers:
        outfile.write(f"{number}\n")