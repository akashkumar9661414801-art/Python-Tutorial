" Write a program to print multiplication table of a given number using for loop."
number=int(input("Enter the number "))
# i=0
# for i in range(1,11):
#     x=number*i
#     print(x)
#     i+=1
for i in range(1,11):
    print(f"{number} x {i}= {number*i}")
