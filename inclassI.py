'''
Thanh Dat Tran, Leo
CIS 41A   Spring 2021
Unit I In-class assignments
'''
import math

# Part 1 Basic Inheritance  Circle & Cylinder

#Circle's __init__ method has the parameters self and radius, and stores the radius as an attribute.
#The getArea method has the parameter self and should return the circle's area
class Circle:
    def  __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return math.pi * pow(self.radius, 2)

class Cylinder(Circle):
    def  __init__(self, radius, height):
        super().__init__(radius)
        self.height = height

    def getVolume(self):
        return super().getArea() * self.height

def main():
    circle1 = Circle(4)
    cylinder1 = Cylinder(2,5)
    print(f"Circle area is: {circle1.getArea():.2f}")
    print(f"Cylinder volume is: {cylinder1.getVolume():.2f}")

if __name__ == '__main__':
    main()

'''
Execution result:
Circle area is: 50.27
Cylinder volume is: 62.83
'''