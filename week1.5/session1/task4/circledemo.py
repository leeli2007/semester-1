# Week 1.5, Session 1: Task 4

# Add one or more import statements here to give this program
# access to the Point and Circle classes defined in geometry.py

# Write a program here that
#  - Creates a Point object, to represent the centre of a circle
#  - Creates a Circle object, using the Point object and a value for radius
#  - Displays the area of the circle
#  - Displays the perimeter of the circle

from geometry import Point,Circle

x = float(input("Enter the x coordinate of the centre: "))
y = float(input("Enter the y coordinate of the centre: "))
centre = Point(x, y)
radius = float(input("Enter the radius: "))
circle = Circle(radius,centre)
print(f"Area: {circle.area():.4f}")
print(f"Perimeter: {circle.perimeter():.4f}")


