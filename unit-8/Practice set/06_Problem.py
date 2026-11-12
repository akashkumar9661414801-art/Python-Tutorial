'''
6. Write a python function which converts inches to cms
'''
def length():
    b=int(input("Enter the length in Inches:-"))
    print(f"Your len in cm is {b*2.54} cm")
length()
#SIMPLE METHOD 
def inch_to_cm (inches):
    return inches*2.54
n=int(input("Enter the value in Inches:-"))
print(f"Thw corresponding value in cm is {inch_to_cm(n)}")