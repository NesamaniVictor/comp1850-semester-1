# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here?
#{"apple", "potato", "orange", "leek", "tomato"}

both = fruit.intersection(vegetables)
print(both)

# Why does the following code diplay five items?
#tomato is repeated

food = fruit.union(vegetables)
print(food)

# Add an item to fruit
fruit.add("grapes")
print(fruit)

# Remove an item from vegetables
vegetables.discard("potato")
print(vegetables)

# Find and display symmetric difference of the two sets
