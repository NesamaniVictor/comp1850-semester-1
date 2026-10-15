# Week 1.3, Session 1: For loop equivalent to a list comprehension

animals = ['dog','cat','hamster','goldfish']

not_fish = [item for item in animals if item != 'goldfish']

print(not_fish)

# species = ["lion" , "tiger" , "spider" , "cat" , "goldfish"]

# not_fish_2 = [things for things in species if things != "goldfish"]

# print(not_fish_2)

# write the equivalent for loop to create the not_fish list from animals
# print your result to verify it is the same

still_not_fish = []
for animal in animals:
    if animal != "goldfish":
        still_not_fish.append(animal)