a=int(input("Enter your age: "))
# If statement no:01
if(a%2==0):
   print("a is even")
# end of If statement no:01
# If statement no:02
if(a>18):
   print("You are above the age of consent")
   print("good for you")

elif(a<0):
   print("you are entering an invalid negative age")
elif(a==0):
   print("you are entering 0 which is not valid")
#end of  If statement no:02
else:
   print ("You are below the age of consent") 
print("End of program")
    