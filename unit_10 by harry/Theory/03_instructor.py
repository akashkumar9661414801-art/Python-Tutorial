class Employee:
    
    lang="py"#this is class attribute
    salary=120000
    def __init__(self,name,salary,lang):
        #dunder method
        self.name=name 
        self.salary=salary 
        self.lang=lang 
        print("I am creating an object")
    def get_info(self):
        print(f"the lang is {self.lang} and the salary is {self.salary}")
    @staticmethod#Decorator
    def greet():
        print("good morning")
harry=Employee("harrry",120000,"python")
print(harry.name)
print(harry.salary)
harry.greet()
ro0han=Employee("Rohan",120000,"python")
