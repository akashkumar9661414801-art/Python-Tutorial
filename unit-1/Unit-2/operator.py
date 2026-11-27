#arithmetic operator 
a=34
b=4
c=a+b
print(c)
#assignment operator
a=4-2 #assingn 4-2 in a 
b=6
b+=3# Increment the value of b  by 3 then assing to b
print(b)
print(type(b))
b-=3# decrement the value of b  by 3 then assing to b
print (b)
print(type(b))
b*=3# decrement the value of b  by 3 then assing to b
print (b)
print(type(b))
b/=3
print(b)
print(type(b))
#comparison operator
# it always return bolean function 
d=5<4
print(d)
d=5>4
print(d)
d=5!=5
print(d)
d=5==5
print(d)
#logical operator
# LOGICAL OR OPERATOR
print("TRUTH TABLE OF OR ")
print("False or False",False or False)
print("False or True",False or True)
print("True or False",True or False)
print("True or True",True or True)

# LOGICAL AND OPERATOR
print("TRUTH TABLE OF AND ")
print("False and False",False and False)
print("False and True",False and True)
print("True and False",True and False)
print("True and True",True and True)

# LOGICAL NOT OPERATOR
print("TRUTH TABLE OF NOT ")
print(not(True))
print(not(False))