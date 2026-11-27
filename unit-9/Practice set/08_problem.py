'''8. Write a program to make a copy of a text file “this.txt”'''
with open ("C:/Users/Akash Kumar/OneDrive/Documents/python/pythoncourse/unit-9/Practice set/this.txt","r") as f:
    Content=f.read()
with open ("C:/Users/Akash Kumar/OneDrive/Documents/python/pythoncourse/unit-9/Practice set/this_copy.txt","w") as f:
    f.write(Content)


