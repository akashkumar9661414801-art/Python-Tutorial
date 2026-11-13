'''5. Repeat program 4 for a list
 of such words to be censored.'''

words=["Donkey","dirty","kyun"]
with  open("C:/Users/Akash Kumar/OneDrive/Documents/python/pythoncourse/unit-9/Practice set/Donkey.txt","r") as f:
    content=f.read()
    for word in words :
     content=content.replace(word,"#"*len(word))
    
with open("C:/Users/Akash Kumar/OneDrive/Documents/python/pythoncourse/unit-9/Practice set/Donkey.txt","w") as f:
    f.write(content)
