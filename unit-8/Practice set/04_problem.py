'''4. Write a recursive function to calculate the sum of first n natural numbers'''
def sum (n):
    # n=int(input("Enter the number:-"))
    if (n==0):
        return 0
    return n+sum(n-1)
n=int(input("Enter the number "))
print(f"The sum of first n natural number is:-{sum(n)}")