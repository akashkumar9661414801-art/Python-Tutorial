a=int(input("Enter a number"))
b=int(input("Enter a second number"))
if(b==0):
    raise ZeroDivisionError("we cant divide a number with zero")
else:
 print(f"The division a/b is{a/b}")