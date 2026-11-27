'''3. Create a class ‘Employeeʼ and add salary and increment properties to it. Write a method
‘salaryAfterIncrementʼ method with a @property decorator with a setter which changes
the value of increment based on the salary'''
class Employee:
    salary=2000
    increement=50
    @property
    def salaryafterincreement(self):
        return self.salary+(self.increement/100)*self.salary
    @salaryafterincreement.setter
    def salaryafterincreement(self,salary):
        self.increement=(salary/self.salary-1)*100
e=Employee()
# print(e.salaryafterincreement)
e.salaryafterincreement=3000
print(e.increement)