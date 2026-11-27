'''Create a class with a class attribute a; create an object from it and set ‘aʼ directly using
‘object.a = 0ʼ. Does this change the class attribute?'''
class Demo:
    a=4
o=Demo()
print(o.a)#prints the class attribute because instance attribute is not present
print(Demo.a)
o.a=3#instance attribute is set
print(o.a)#print the instance attrubute because instance attribute is present
print(Demo.a)#class attribute doesny change