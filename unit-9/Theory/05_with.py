f=open("Theory/file.txt")
print(f.read())
f.close()
#The same canbe wriiten using with statement like this:
with open ("Theory/file.txt") as f:
    print(f.read())
#you dont have to close the file  
