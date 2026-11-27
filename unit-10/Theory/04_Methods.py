class Student():
    #Parameterized Constructer
    def __init__(self,fullname):
        self.fullname=fullname
    #Function inside class is called as method 
    def Hello(self,age):
        self.age=age
        print("Hello",self.fullname,self.age)
#Creting Object
S1=Student("Akash Kumar")    
S1.Hello(23)   