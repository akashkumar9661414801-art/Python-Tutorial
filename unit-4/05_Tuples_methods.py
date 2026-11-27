a=(1,45,342,3424,False,"Rohan","Shivam",45,45,45)
print(a)
print(a.count(45))#it will count hte number of occurence
print(a.index(45))#it will give the first occurnce 
print(len(a))#it will give the length of tuples
print(type(a[4]))
a1=(1,45,342,3424,45,45,45)
print(max(a1))
print(sum(a1))
print(sorted(a1))#sort elements into list 
print(list(a))#converts tuple to list
c = (10, 20, 30)
b = (40, 50)

print(c + b)       # Concatenation
print(c * 2)       # Repetition
print(20 in c)     # Membership
print(c[0])        # Indexing
print(c[1:3])      # Slicing
fruits = ("Apple", "Mango", "Orange")

for index, fruit in enumerate(fruits):
    print(index, fruit)