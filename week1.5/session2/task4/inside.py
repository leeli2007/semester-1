# Week 1.5, Session 2: Task 4

# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class
from geometry import Point, Circle

p = Point(3,4)
c = Circle(5, Point(0, 0))  
print(p in c)

p = Point(1,2)
c = Circle(3, Point(0, 0))
print(p in c)