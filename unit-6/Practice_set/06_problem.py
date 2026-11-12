'''Write a program to calculate themarks of a student from his marks from the following
scheme:
90 – 100 => Ex
80 – 90 => A
70 – 80 => B
60 – 70 => C
50 – 60 => D
<50 => F'''
marks=int(input("Enter the marks of student: "))
if(marks<100):
    print("Your gradeis Ex")
elif(marks<90):
    print("Your grade is  A ")
elif(marks<80):
    print("Your grade is  B ")
elif(marks<70):
    print("Your grade is  C ")
elif(marks<60):
    print("Your grade is  D ")
else:
    print("FAIL")