''' Write a class “Calculator” capable of 
finding square, cube and square root of a number.'''
class cal:
    def __init__(self,Num):
        self.Num=Num
    def Square(self):
        print(f"your Num is {self.Num}")
        print(f"Square of {self.Num} is {self.Num**2}")
    def cube(self):
        print(f"your Num is {self.Num}")
        print(f"Cube of {self.Num} is {self.Num**3}")
    def SquareRoot(self):
        print(f"your Num is {self.Num}")
        print(f"Squareroot of {self.Num} is {self.Num**0.5}")
   
        
num1=cal(2)
num1.Square()
num1.SquareRoot()
num1.cube()