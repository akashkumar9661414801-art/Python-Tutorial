''' Write a program to open three files 1.txt, 2.txt and 3.txt. If any of these files are not
present, a message without exiting the program must be printed prompting the same.'''
try:
    with open("C:/python/pythoncourse/Python-Tutorial/unit-12/Practice Set/1.txt") as f:
     print("File 1.txt is present")
except FileNotFoundError:
     print("File is not present")
try:
    with open("C:/python/pythoncourse/Python-Tutorial/unit-12/Practice Set/2.txt") as f:
     print("File 2.txt is present")
except FileNotFoundError:
     print("File 2.txt is not present")
try:
    with open("C:/python/pythoncourse/Python-Tutorial/unit-12/Practice Set/3.txt") as f:
     print("File 3.txt is present")
except FileNotFoundError:
     print("File 3.txt is not present")
