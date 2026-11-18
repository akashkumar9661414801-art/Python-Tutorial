class Employee:
    
    lang="py"#this is class attribute
    salary=120000
harry=Employee()
harry.name="Harry"#this is an object/instance attribute
print(harry.name,harry.lang,harry.salary,sep="\n")

rohan = Employee()
rohan.name="Rohan "
rohan.lang="java"#instance attribute take prefrence 
print(rohan.name,rohan.salary,rohan.lang,sep="\n")
'''Here name is object atttibute and salary and languge are class attribute as they directly 
belong to the class'''