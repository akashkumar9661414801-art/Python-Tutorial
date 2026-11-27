'''Define a Circle class to create 
a circle with radius r using the constructor 
Define an Area() method of the class which 
calculates the area of the cirle 
Define a perimeter()method of the class 
which allows you to calculate the perimeter 
of the circle'''
class circle:
    def __init__(self,radius):
        self.radius=radius
    def Area(self):
        return (22/7)*self.radius**2
    def perimeter(self):
        return 2*(22/7)*self.radius
c1=circle(21)
print(c1.Area())
print(c1.perimeter())
    