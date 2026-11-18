class Person:
    name="Anonymous"
    # def changeName(self,name):
    #     Person.name=name
    @classmethod
    def changeName(cls,name):
        cls.name=name
p1=Person()
p1.changeName("Akash Kumar")
print(p1.name)
print(Person.name)