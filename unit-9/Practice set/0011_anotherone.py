'''1.Write a program to read the text from a given file ‘poems.txtʼ and find out whether it
contains the word ‘twinkleʼ
but i wanna check each line and print yes for each line 

'''
word="twinkle"
with open ("Practice set/poems.txt","r") as f:
    # for line in f:
    #     if word in line:
    #         print("Yes")
    #     else:
    #         print("NO")
        for num, line in enumerate(f, start=1): 
         if word in line:
             print("Line", num, ": Yes")
         else:
             print("Line", num, ": No")
        '''here enumerate function is used to both the index and value of elements while 
        iterating through a sequence (like a list, tuple, or string).'''
