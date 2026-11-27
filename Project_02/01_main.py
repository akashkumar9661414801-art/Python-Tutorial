'''We are going to write a program that generates a random number and asks the user to
guess it.
If the playerʼs guess is higher than the actual number, the program displays “Lower
number please” .
Similarly, if the userʼs guess is too low, the program prints “Higher number please” .
When the user guesses the correct number, the program displays the number of
guesses the player used to arrive at the number'''
import random
n=random.randint(1,10)
a=-1
gueses=0
while(a!=n):
 gueses+=1
 a=int(input("Guess the number: "))
 if(a==n):
  print(f"yay! your num {a} and computer num is {n} \n you guessed it right")
  break
 if(a>n):
  print("you number is higher than  computer number ")
  
 else:
  print("you number is lower than  computer number ")
print(f"you have guessed the number in {gueses} attempt")
  