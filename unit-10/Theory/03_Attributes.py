'''There are two type of attributes 
1. Class attribut:- Common for all 
2.Instances attribute:-different of all 
and priority of obj attr>>>Class attribute'''
class Student:
    CollegeName="ABC College"#Class Attribute
    name="College"#Class Attribute
    #Defualt constructor 
    def __init__(self):
        pass
    # name="Akash Kumar"

        
    #Parameterized Constructor 
    def __init__(self,fullname="Kash",age=15):
        self.name = fullname#Instances attribute
        self.age=age#Instances Attributes
        print(self)
        print("Adding new student in Database")
S1=Student("Akash Kumar",21)
print(S1.name,S1.age,Student.CollegeName,Student.name,sep="\n") #Akash Kumar 21 ABC College College 
S2=Student("Shubham",22)
print(S2.name,S2.age,Student.CollegeName)
S3=Student()
print(S3.name) 