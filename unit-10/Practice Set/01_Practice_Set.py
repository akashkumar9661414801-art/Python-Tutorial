'''Create student class that takes name and marks
of 3 subjects as arguments in constructor
then create a method to print the avg'''
class Student():
    def __init__(self,Name,Marks):
        self.Name=Name
        self.Marks=Marks
    @staticmethod#Decorator 
    #STATIC METHOD 
    def greet():
        print("Hello")
    def avg(Self):
        sum=0
        n=0
        for val in Self.Marks:
            sum+=val
            n+=1
        print(f"Hi Your name is {Self.Name} and you avg score is {sum/n}")
S1=Student("Alka",[34,67,78,65])
S1.avg()
S1.greet()
#     def __init__(self,name,marks1,marks2,marks3):
#         self.name=name
#         self.marks1=marks1
#         self.marks2=marks2
#         self.marks3=marks3
#     def avg(self):
#         print(f"The avg of subject is {(self.marks1+self.marks2+self.marks3)/3}")
# S1=Student("Akash kumar",78,78,78)
# S1.avg()
