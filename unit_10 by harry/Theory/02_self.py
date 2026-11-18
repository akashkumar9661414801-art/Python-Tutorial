class Employee:
    
    lang="py"#this is class attribute
    salary=120000
    def get_info(self):
        print(f"the lang is {self.lang} and the salary is {self.salary}")
    @staticmethod#Decorator
    def greet():
        print("good morning")
harry=Employee()
harry.get_info()
harry.greet()

