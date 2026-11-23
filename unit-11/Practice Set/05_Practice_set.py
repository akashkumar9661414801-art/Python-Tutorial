'''Write a class vector representing a vector of n dimensions. Overload the + and * operator
which calculates the sum and the dot(.) product of them'''
class vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self, other):
        return vector(self.x+other.x,self.y+other.y,self.z+other.z)
        
    def __mul__(self, other):
        result=self.x*other.x+self.y*other.y+self.z*other.z
        return result
    def __str__(self):
        return f"{self.x}x+{self.y}y+{self.z}z"
v1=vector(1,4,5)
v2=vector(2,6,8)
print(v1+v2)
print(v1*v2)