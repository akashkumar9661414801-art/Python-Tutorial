#name slicing
name=" akash kumar"
# nameshort= name[0:3]#strt from index 0 till 3 excluding 3 
# print(nameshort)
# print(name[0:3])
# print(name[-5:-2])
# print(name[:4])#same as print(name[0:4])
# print(name[0:4])
# print(name[1:]) #same as print(name[1:5])
# print(name[1:5])
#slicing with skip value
print(name[1:5:2])#this 2 tells we are taking 2nd val after removing
print(len(name))
print(name.endswith("sh"))
print(name.startswith("Aka"))
print(name.capitalize())
print(name.title( )) #capitalize the first letter of each word
print(name.strip())#removes the trailing  and leading  space in the word
index=name.find("ku")
index2=name.replace("ku","gu")
print(index)
print(index2)