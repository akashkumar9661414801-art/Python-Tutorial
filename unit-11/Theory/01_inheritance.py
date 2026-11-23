class Employee:
    company ="ITC"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salry is {self.salary}")
# class programmer:
#     company="ITC Infotech"

#     def show(self):
#             print(f"The name is {self.name} and the salry is {self.salary}")
#     def showlang(self):
#          print(f"The name is {self.name} and he is good with {self.lang} language ")        
class programmer(Employee):
    company="ITC Infotech"
    def showlang(self):
        print(f"The name is {self.name} and he is good with {self.lang} language ")

a=Employee()
b=programmer()
print(a.company,b.company)