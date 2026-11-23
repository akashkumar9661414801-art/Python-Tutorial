l=[3,5,67,89]
# index=0
# for item in l:
#     print(f"The item number at {index} is {item}")
#     index+=1


#This can be simplified using enumerate function
for index,item in enumerate(l):
    print(f"The item number at {index} is {item}")