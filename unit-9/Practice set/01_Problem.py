'''1.Write a program to read the text from a given file ‘poems.txtʼ and find out whether it
contains the word ‘twinkleʼ'''
word="twinkle"
with open ("Practice set/poems.txt") as f:
    content=f.read()
    if word in content:
        print("Yes")
    else:
        print("NO")
                 