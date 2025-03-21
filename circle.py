"""Create a class named Circle and intialize it with radius. Make two methods 
getArea (to return area of a circle) and geCircumference (to return the 
circumference of the circle )inside this class"""
class Circle:
    def __init__(self, radius):
        self.radius = radius  # Initialize the radius
    
    def getArea(self):
        return 3.1416 * self.radius * self.radius  # Return area of the circle
    
    def getCircumference(self):
        return 2 * 3.1416 * self.radius  # Return circumference of the circle
