''' Write a program using functions to find greatest of three numbers.'''
def max():
    a=int(input("Enter the number"))
    b=int(input("Enter the number"))
    c=int(input("Enter the number"))
    if(a>b and a>c):
        print(f"maximum number is {a}")
    elif(b>a and b>c):
        print(f"maximum number is {b}")
    else:
        print(f"maximum number is {c}")
max()