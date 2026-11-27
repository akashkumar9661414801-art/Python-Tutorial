n=int(input("Enter the number of row "))
for i in range(1,(2*n)):
    if(i<n+1):
        print("*"*i)
    else:
        print("*"*((2*n)-i))