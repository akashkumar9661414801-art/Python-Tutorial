#7. If the names of 2 friends are same; what will happen to the program in problem 6?
d={}
name=input("Enter the Friends name: ")
lang=input("Enter the language name: ")
d.update({name:lang})
name=input("Enter the Friends name: ")
lang=input("Enter the language name: ")
d.update({name:lang})
name=input("Enter the Friends name: ")
lang=input("Enter the language name: ")
d.update({name:lang})
name=input("Enter the Friends name: ")
lang=input("Enter the language name: ")
d.update({name:lang})
print(d)
#then it will update the languge of first occurence to next occurence
#and it will print only three key and their key value