'''2. Write a program to greet all the person names stored in a list ‘lʼ and which starts with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]'''
l = ["Hasrry", "Soham", "Sachin", "Rahul"]
# for i in  range (len(l)):
#     if "s" in (l[i]).lower():
#         print("hello",l[i])
#         i+=1
#     else:
#         print(" ")
 
for name in l:
    if(name.startswith("S")):
        print(f"Hello{name}")