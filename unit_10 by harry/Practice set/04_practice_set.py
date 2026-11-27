''' Add a static method in problem 2, to greet the user with hello'''
class cal:
    def __init__(self,Num):
        self.Num=Num
    @staticmethod
    def greet():
        print("Hello")
    def Square(self):
        self.greet()
        print(f"your Num is {self.Num}")
        print(f"Square of {self.Num} is {self.Num**2}")
    def cube(self):
        self.greet()
        print(f"your Num is {self.Num}")
        print(f"Cube of {self.Num} is {self.Num**3}")
    def SquareRoot(self):
        self.greet()
        print(f"your Num is {self.Num}")
        print(f"Squareroot of {self.Num} is {self.Num**0.5}")
   
        
num1=cal(2)
num1.Square()
num2=cal(4)
num2.cube()