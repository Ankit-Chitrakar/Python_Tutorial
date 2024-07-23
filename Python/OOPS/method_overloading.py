# in python method overloading did not work directly
import math
class Geometry:
    def area(self, a, b=0):
        if b == 0:
            return math.pi * (a ** 2)
        else:
            return a * b
    
circle = Geometry()
print(circle.area(5))

rectangle = Geometry()
print(rectangle.area(5, 10))

# This gives error
# so what we do we wioll change area method 