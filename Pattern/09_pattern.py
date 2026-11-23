n=int(input("Enter the number of row "))
for i in range(1,2*n):
     if(i<n+1):
            print(" "*(n-i)+"*"*i)
     else:
            print(" "*(i-n)+"*"*((2*n)-i))