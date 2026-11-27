'''Data Type'''
import numpy as np
#for number
var=np.array([1,2,3,4,12,3,15])
print("Data Type:",var.dtype)
#Float number
var1=np.array([1.2,0,3.5,4,1,3,15])
print("Data Type:",var1.dtype)
#String Datatype
var3=np.array(["a","b","d"])
print("Data Type:",var3.dtype)
#String and Number
var3=np.array(["a","b","d",1,2,3])
print("Data Type:",var3.dtype)
#conversion of datatype
x=np.array([1,2,3,4],dtype=np.int8)
print("Data Type:",x.dtype)
#conversion of datatype using shortcut key
y=np.array([1,2,3,4],dtype="f")
print("Data Type:",y.dtype)
#data conversion using function
z=np.array([1,2,3,4])
new=np.float32(z)
new1=np.int_(new)
print(z)
print("Data Type:",z.dtype)
print(new)
print("Data Type:",new.dtype)
print(new1)
print("Data Type:",new1.dtype)
#Directly conversion of DataType using astype
a=np.array([1,2,3,4,5])
print(a)
print("Data Type:",a.dtype)

new_1=a.astype(float)
print(new_1)
print("Data Type:",new_1.dtype)
