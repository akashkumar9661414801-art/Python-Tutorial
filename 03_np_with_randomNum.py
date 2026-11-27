#Rand()
import numpy as np
var=np.random.rand(4)
#rand() takes the value between 0to1
print(var)
Var1=np.random.rand(1,5)
print(f"Your array is{Var1}")
#randn() close tp zero it will be +ve and-ve number
va2=np.random.randn(2,3)
print(f"your var2 is{va2}")
#ranf random variable between[0.0,1.0)
var3=np.random.rand(3,4)
print(f"your var3 is {var3}")
#randint random number in between given range (min,max,max number to generate)
var4=np.random.randint(1,5,5)
print(f"your var4 is {var4}")
