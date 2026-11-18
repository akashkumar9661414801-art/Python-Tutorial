#parent class of ToyataCar
class Car:
    @staticmethod
    def Start():
        print("car started..")
    @staticmethod
    def stop():
        print("car stoppped..")
#SINGLE LEVEL INHERITANCE
#Child Class and then Parent of Class Fortuner
class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand=brand
#Child CLass of ToyataCar
class Fortuner(ToyotaCar):
    def __init__(Self,Type):
        Self.type=Type
        print(Self.type)
car1=Fortuner("Diesel")
car1.Start()


'''Now it is multilevel INHERITANCE'''

'''due to inheritance it can take the
property of parent class'''
    