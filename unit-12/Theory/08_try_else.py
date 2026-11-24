try:
    a=int(input("Enter the number: "))
    print(a)

except Exception as e:
    print(e)
else:
    print("I am inside else and try was succesfully run ")
'''Sometimes we wanna run a piece of code when try was succesful'''
