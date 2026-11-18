'''Create a class “Programmer” for storing information of few programmers working at
Microsoft'''
class Programmer:
    company="Microsoft"
    def __init__(self,Name,age,language,salary):
        self.Name=Name
        self.age=age
        self.lan=language
        self.salary=salary
    def get_info(self):
        print(self.Name,self.age,self.lan,self.salary,self.company,sep="\n")
p1=Programmer("Akash",21,"Python",120000)
p1.get_info()