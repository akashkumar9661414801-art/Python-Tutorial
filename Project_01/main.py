import random 
'''
1 for snake
-1 for water 
0 for gun
'''
computer=random.choice([-1,0,1])
youstr=input("Enter your choice:-")
youdict={"s":1,"w":-1,"g":0}
reversedict={1:"Snake",-1:"Water",0:"Gun"}
you=youdict[youstr]
print(f"You choose {reversedict[you] } \nComputer choose {reversedict[computer]}")
if (computer==you):
    print("It's DRAW")
else:
    if(computer==1 and you==0):
        print("You Win")
    elif(computer==1 and you==-1):
        print("You loose")
    elif(computer==0 and you==-1):
        print("You win")
    elif(computer==0 and you==1):
        print("You loose")
    elif(computer==-1 and you==1):
        print("You win")
    elif(computer==-1 and you==0):
        print("You loose")
    else :
        print("Something is Wrong ")
    

