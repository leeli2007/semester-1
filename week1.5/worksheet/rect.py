# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)

        if not isinstance(width,int):
            raise TypeError("Width must be integer")

        if not isinstance(height,int):
            raise TypeError("Height must ba integer")

        if width <= 0:
            raise ValueError("Width must be greater than 0")

        if height <= 0:
            raise ValueError("Height must ba greater than 0")

        self.width = width
        self.height = height
        
    # Implement methods is_square(), area() & perimeter() here
    # (See README.md for details of what they should do)
    def is_square(self):
        '''
        Check if the pattern is square or rectangular
        '''
        if self.width == self.height:
            return True
        else:
            return False

    def area(self):
        '''
        Calc pattern area
        '''
        return self.width * self.height

    def perimeter(self):
        '''
        Calc pattern perimeter
        '''
        return self.width * 2 + self.height * 2    