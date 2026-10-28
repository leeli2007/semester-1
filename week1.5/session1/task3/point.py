# Week 1.5, Session 1: Task 3
import math
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


# Finally, add code here to demonstrate use of Point
p1 = Point(0,3)
p2 = Point(4,0)
print(p1.distance())
print(p1.distance_to(p2))