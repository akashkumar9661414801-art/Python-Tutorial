#Write a program to find the greatest of four numbers entered by the user.
a=int(input("Enter your first number: "))
b=int(input("Enter your second number: "))
c=int(input("Enter your third number: "))
d=int(input("Enter your fourth number: "))
if(a>b and a>c and a>d):
    print("a is  greater that is:-",a)
elif(b>a and b>c and b>d):
    print("b is  greater that is:-",b)
elif(c>a and c>b and c>d):
    print("c is  greater that is:-",c)
else:
    print("d is  greater that is:-",d)