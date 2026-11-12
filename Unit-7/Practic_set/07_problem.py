#6. Write a program to calculate the factorial of a given number using for loop
#5!=1x2x3x4x5
n=int(input("Enter the number "))
i=1
prod=1
for i in range(i,n+1):
    prod=prod*i
    i+=1
print(f"the factorial of {n} is {prod}")
