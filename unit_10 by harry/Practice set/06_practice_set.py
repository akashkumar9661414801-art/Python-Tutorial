'''Can you change theharrry-parameter inside a class to something else (say “harry”)? Try
changingharrry to “slf” or “harry” and see the effects.'''
class Programmer:
    company="Microsoft"
    def __init__(harry,Name,age,language,salary):
        harry.Name=Name
        harry.age=age
        harry.lan=language
        harry.salary=salary
    def get_info(harry):
        print(harry.Name,harry.age,harry.lan,harry.salary,harry.company,sep="\n")
p1=Programmer("Akash",21,"Python",120000)
p1.get_info()