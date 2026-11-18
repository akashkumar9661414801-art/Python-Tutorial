class Car:
    def __init__(self,type):
        self.type=type
        
    @staticmethod
    def Start():
        print("car started..")
    @staticmethod
    def stop():
        print("car stoppped..")
#SINGLE LEVEL INHERITANCE
#Child Class and then Parent of Class Fortuner
class ToyotaCar(Car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)
        super().Start
#super method is used to access method of the oarent class 
car1=ToyotaCar("Prius","Electric")
print(car1.type,car1.Start())
