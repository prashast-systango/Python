# importing parent class
from inherited import Area

# Child class
class Shape(Area):
    def triangle(self, base, height):
        self.area = (base*height)/2
        super().area("Area of Triangle :",self.area)

    def circle(self,radius):
        self.pi = 3.14
        self.area = self.pi*(radius*radius)
        super().area("Area of Circle :",self.area)

    def square(self,side):
        self.area = (side*side)
        super().area("Area of Square :",self.area)

    def rectangle(self, length, breadth):
        self.area = (length*breadth)
        super().area("Area of Rectangle :",self.area)   

obj = Shape()

obj.triangle(20,20)
obj.circle(4)
obj.rectangle(4,7)
obj.square(5)