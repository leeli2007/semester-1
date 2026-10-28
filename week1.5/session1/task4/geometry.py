# Week 1.5, Session 1: Task 4

"""
Classes for working with two-dimensional geometry.
"""

import math

# Copy Point class definition here

# Add a definition for a Circle class here, giving it
#  - A constructor that creates fields to represent the centre & radius
#    of a circle (assume centre is represented as a Point object)
#  - A method area(), returning the area of the circle
#  - A method perimeter(), returning the perimeter of the circle

# Don't add any testing code to this file!
class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self,x_coordinate,y_coordinate):
        self.x = x_coordinate
        self.y = y_coordinate

    # Add distance() method here
    def distance(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    # Add distance_to() method here
    # (This will need a parameter representing another point)
    def distance_to(self,pt2):
        dx = pt2.x - self.x
        dy = pt2.y - self.y
        return math.sqrt(dy**2 + dx**2)

class Circle:
    radius = 0 
    centre = Point(0,0)

    def __init__(self,radius,centre=Point(0,0)):
        self.radius = radius
        self.centre = centre

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return math.pi * self.radius * 2
  
