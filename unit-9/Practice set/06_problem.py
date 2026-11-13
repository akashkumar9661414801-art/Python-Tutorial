'''6. Write a program to mine a log file and 
find out whether it contains ‘pythonʼ.'''
word="python"
with open ("C:/Users/Akash Kumar/OneDrive/Documents/python/pythoncourse/unit-9/Practice set/log.txt","r") as f:
    content=f.read()
    if word in content :
        print("yes ")
    else:
        print ("no")