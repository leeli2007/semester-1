# Week 1.6, Session 1: Task 3

# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)
from shapes import Circle
from point import Point

pos = Point(0.0,0.0)
c = Circle(2.5,pos)
print(c)

print(f"Area = {c.area():.3f}")
print(f"Perimeter = {c.perimeter():.3f}")

# Change the position
print("Moving the circle...")
c.position = Point(1.6, 3.2)
print(c)

# Change the colour
print("Changing the circle's colour...")
c.colour = "green"
print(c)