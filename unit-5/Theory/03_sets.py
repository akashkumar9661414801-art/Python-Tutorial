s={1,4,5,66,6,67,6,7,8,"Harry"}
e=set()#Dont use s={}as it will create an empty dictionatry
print(s,type(s))
s.add(4555)#Adds one element
print(s,type(s))
s.update({56,67,89})#Adds multiple elements
print(s,type(s))
s.remove("Harry")#Removes an element; error if absent
print(s,type(s))
s.discard("ak")#Removes an element without error if absent
print(s,type(s))
s.pop()
print(s,type(s))#Removes and returns an arbitrary element
# s.clear()
# print(s,type(s))#Removes all elements
