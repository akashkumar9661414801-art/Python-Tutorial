'''Write a program to print third, fifth and seventh element from a list using enumerate
function'''
l=[1,2,3,4,5,6,7]
for index,item in enumerate(l,start=1):
    if (index==3 or index==5 or index ==7):
        print(item)
