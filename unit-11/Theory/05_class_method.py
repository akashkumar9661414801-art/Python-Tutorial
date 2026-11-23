class Employee:
    a=1
    @classmethod
    def show(cls):
        print(f"The class value of a is {cls.a}")
e=Employee()
e.a=45
e.show()#prints the class value of a is 1 because class method is called by class name