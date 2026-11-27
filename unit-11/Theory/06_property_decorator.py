class Employee:
    a=1
    @classmethod
    def show(cls):
        print(f"The class value of a is {cls.a}")
    @property
    def name(self):
        return self.ename
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
e=Employee()
e.a=45
e.show()#prints the class value of a is 1 because class method is called by class name
e.name = "Akash Kumar"
print(e.fname)#prints Akash
print(e.lname)#prints Kumar