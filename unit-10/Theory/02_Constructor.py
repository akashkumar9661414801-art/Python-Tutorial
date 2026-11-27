class Student:
    #Defualt constructor 
    def __init__(self):
        pass
    # name="Akash Kumar"

        
    #Parameterized Constructor 
    def __init__(self,fullname,age):
        self.name = fullname
        self.age=age
        print(self)
        print("Adding new student in Database")
S1=Student("Akash Kumar",21)
print(S1.name,S1.age,sep="\n") #Akash Kumar 21
S2=Student("Shubham",22)
print(S2.name,S2.age)
'''Self parameter is a refrences to the current 
instances of the class, and is used to acces variables
that belongs to the class'''
