class Employee:
    a=1
class Programmer(Employee):
    b=2
class Manager(Programmer):
    c=3
o=Employee()
print(o.a)#prints the a attribute of Employee class
#print(o.b)#shows error because b is not present in Employee class
o=Programmer()
print(o.a,o.b)#prints the a attribute of Employee class
#print(o.c)#shows error because c is not present in Programmer class
o=Manager()
print(o.a,o.b,o.c)#prints the a, b, and c attributes of Employee, Programmer, and Manager classes respectively class
