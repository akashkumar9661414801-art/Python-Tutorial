'''
5. Write a python function to print first n lines of the following pattern.
***
**
*
'''
def patt():
    n=int(input("Enter the number of Row:-"))
    for i in range (0,n+1):
        print("*"*(n-i))
#IN RECURRSIVE METHOD 
def pat(r):
   
    if(r==0):
        return
    print("*"*r)
    pat(r-1)
           

patt()
pat( r=int(input("Enter the number of ROWs:- ")))