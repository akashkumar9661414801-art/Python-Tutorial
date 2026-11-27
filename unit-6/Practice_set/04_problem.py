'''Write a program to find whether a given username contains less than 10 characters or not.'''
username=input("Enter the Username: ")
a=len(username)
if(a>10):
    print("Username contains more than 10 charcter")
else:
    print("This username contains less than 10 charcter")