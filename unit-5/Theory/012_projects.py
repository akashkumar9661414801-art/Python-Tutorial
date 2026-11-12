for row in range(6):
    for col in range(6):
        if (row==col):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()#it will print heart shape 
