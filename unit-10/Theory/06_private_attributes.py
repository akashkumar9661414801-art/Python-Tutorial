class Person:
    __name="Akash"
    # print(__name)
    def __hello(self):
        print("hello person")
    def Welcome(self):
        self.__hello()
        
P1=Person()
# print(P1.__name)
print(P1.Welcome())
'''It will give an errror because __name becomes
private and it will work in Class only'''
'''private attributes and methods are meant to be
only within the class and are not accessible from
outside the class'''
