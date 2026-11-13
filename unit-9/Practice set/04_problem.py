'''4. A file contains a word “Donkey”
 multiple times. You need to
 write a program which
replaces this word with ##### by 
updating the same file'''
word="Donkey"
with  open("C:/Users/Akash Kumar/OneDrive/Documents/python/pythoncourse/unit-9/Practice set/Donkey.txt","r") as f:
    content=f.read()
    content=content.replace("#####",word)
    
with open("C:/Users/Akash Kumar/OneDrive/Documents/python/pythoncourse/unit-9/Practice set/Donkey.txt","w") as f:
    f.write(content)


        
