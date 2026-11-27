'''2. The game() function in a program lets a user play a game and 
returns the score as an
integer. You need to read a file ‘Hi-score.txtʼ which is either
 blank or contains the previous
Hi-score. You need to write a program to update the Hi-score 
whenever the game() function breaks the Hi-score'''
import random

def game():
    print("You are playing a game ")
    score=random.randint(1,64)
    #this function randint is use to select the number in given range 

#Fetch the score from txt file 
    with open ("Practice set/hiscore.txt") as f :
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0
    print(f"Your score is {score} ,and previous high score is {hiscore}")


    if (score>hiscore):
#write in file
         with open ("Practice set/hiscore.txt","w") as f :
             f.write(str(score))
    return((score))
game()