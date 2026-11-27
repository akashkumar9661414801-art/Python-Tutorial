#Write a program to find whether a given number is prime or not.
number=int(input("enter your number: "))
i=2
if(number==0 or number==1):
    print("number is neither prime nor composite")
while(i<number):
    if(number%i==0):
        print("number is not prime")
        i+=1
        break
    else:
        print("number is prime")
    break
