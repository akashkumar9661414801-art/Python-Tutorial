friends=["Apple","orange",5,34.05,False,"Akash"]
friends.append("Aka")
print(friends)
friends.insert(4,"SUR")#it will add SUR in the fourth place 
print(friends)
friends.remove("SUR")#it will remove SUR from list 
print(friends)
num=[1,5,8,9,10,65,79]
num.sort#(reverse=False)#by default it will sort in assescending order
print(num)
#num.sort(reverse=True)
num.reverse()
print(num)
num.insert(3,33333)
print(num)
print(num.pop(2))#it will popout the number at index 2 which is 10
print(num)

##i wanna replace every 30 in list numbers
#numbers = [30, 20, 30, 10, 5]
#for i in range(len(numbers)):
#    if numbers[i] == 30:
#        numbers[i] = 45
#
#print(numbers)