def myfunc():
    print("Hello World")
from module import myfunc
if __name__=="__main__":
    #If this code is directly executed by running the file its present in 
    print("we are directly running this code")
    myfunc()
    print(__name__)

