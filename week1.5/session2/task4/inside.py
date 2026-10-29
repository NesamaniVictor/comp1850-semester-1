# Week 1.5, Session 2: Task 4

# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class

from geometry import Point, Circle

circle = Circle(5, Point(0, 0))
inside_point = Point(3, 3)
outside_point = Point(6, 0)

print(inside_point in circle)
print(outside_point in circle)