# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here

class Point:
    """
    A Point in 2D space.
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        return math.hypot(self.x, self.y)
   
    def distance_to(self, point):
        """
        Returns distance from this point to the specified point.
        """
        return math.hypot(self.x - point.x, self.y - point.y)

p = Point(1.5, 4.2)
q = Point(3.7, 2.6)

print(p.distance_to(q))

class Circle:
    """
    A circle, with a radius and centre coordinates.
    """

    def __init__(self, radius, centre=Point(0.0, 0.0)):
        """
        Creates a Circle object, with the given radius and centre coordniates.
        Centre coordinates default to the origin.
        """
        self.radius = radius
        self.centre = centre

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius
    

# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle

# Don't add any testing code to this file!
