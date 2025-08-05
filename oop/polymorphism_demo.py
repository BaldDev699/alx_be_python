# Script demonstrating polymorphism with shapes

# importing necessary libraries
import math

# Base class for shapes
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

# Class for Rectangle inheriting from Shape    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Class for Circle inheriting from Shape    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)