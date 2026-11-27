'''Create a class (2-D vector) and use it to 
create another class representing a 3-D vector.'''
class TwoDvector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
        print(f"your vector is {self.i}i+{self.j}j")
class ThreeDvector(TwoDvector):
    def __init__(self, i, j,k):
        self.k=k
        super().__init__(i, j)
        print(f"The vector is {self.i}i+{self.j}j+{self.k}k")
a=TwoDvector(56,65)
b=ThreeDvector(1,3,5)