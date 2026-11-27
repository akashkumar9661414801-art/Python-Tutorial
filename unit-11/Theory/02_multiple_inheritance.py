class Employee:
    company ="ITC"
    def show(self):
        print(f"The company name of the Employee is {self.company} and the language is {self.language}")
class coder:
    language="Python"
    def printlanguage(self):
        print(f"Out of all the languages here is your language{self.language}")
# class programmer:
#     company="ITC Infotech"

#     def show(self):
#             print(f"The name is {self.name} and the salry is {self.salary}")
#     def showlang(self):
#          print(f"The name is {self.name} and he is good with {self.lang} language ")        
class programmer(Employee,coder):
    company="ITC Infotech"
    def showlang(self):
        print(f"The company name is {self.company} and he is good with {self.language} language ")

a=Employee()
b=programmer()
print(a.company,b.company)
b.show()
b.showlang()
b.printlanguage()