'''Write a program to find out whether a student has passed or failed if it requires a total of
40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an
input from the user.'''
a1=int(input("Enter the marks of first subject: "))
a2=int(input("Enter the marks of second subject: "))
a3=int(input("Enter the marks of third subject: "))
total=((a1+a2+a3)/300)*100
print(total)
if(a1>=33 and a2>=33 and a3>=33 and total>=40):
    print("PASSED",total)
else:
    print("FAILED",total) 