a=81
def fun():
    global a#global variable changes from 81 to 3

    a=3
    print(a)
fun()
print(a)