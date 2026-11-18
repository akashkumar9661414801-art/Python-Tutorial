'''Define a employee class with attributes role,Department 
and salary. This class also a ShowDetails()
method
crete an eengineer class that inherits 
properties from employee and has additional
attributes:name and age'''
class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
    def ShowDetails(self):
        print(self.role)
        print(self.dept)
        print(self.salary)
class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT",40000)
        
Employee1=Engineer("Akash",21)
print(Employee1.ShowDetails())
