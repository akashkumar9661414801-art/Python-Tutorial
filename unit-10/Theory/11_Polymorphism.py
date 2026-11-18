'''When the same operator is allowed to have 
different meaning according to the context'''
# print(1+2)#3
# print("Akash"+" Kumar")#concatenate
# print([1,2,3]+[4,5,6])#merge
class Complex:
    def __init__(self,Real,img):
        self.Real=Real
        self.img=img
    def ShowNum(self):
        print(self.Real,"i+",self.img,"j")
    # def add (self,num1):
    #     newReal=self.Real+num1.Real
    #     newImg=self.img+num1.img
    #     return Complex(newReal,newImg)
    def __add__ (self,num1):#Dunder function __add__
        newReal=self.Real+num1.Real
        newImg=self.img+num1.img
        return Complex(newReal,newImg)
    def __sub__ (self,num1):#Dunder function __sub__
        newReal=self.Real-num1.Real
        newImg=self.img-num1.img
        return Complex(newReal,newImg)

num=Complex(45,56)
num.ShowNum()
num1=Complex(5,6)
num1.ShowNum()
num2=num+num1
num2.ShowNum()
num3=num-num1
num3.ShowNum()
