'''2. Write a program to greet all the person names stored in a list ‘lʼ and which starts with S.
l = ["Harry", "Soham", "Sachin", "Rahul"] using While loop'''
l = ["Harry", "Soham", "Sachin", "Rahul"]
i=0
while (i<len(l)):
    if "s" in (l[i]).lower():
        print("hello",l[i])
    i+=1


