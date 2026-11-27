import numpy as np
#1st Dimensional Array
x=[1,2,3,4]
y=np.array([1,2,3,4,5])
print(y)
print(type(y))
print(y)
print(y.ndim)#ndim gives the dimension of array
#2nd Dimensional Array
ar2=np.array([[1,2,3,4],[1,2,3,5]])
print(ar2)
print(type(ar2))
print(ar2.ndim)
#3rd Dimensional Array
ar3=np.array([[[1.1,1.2,1.3,1.4],[2.1,2.2,2.3,2.4],[3.1,3.2,3.3,3.4],[4.1,4.2,4.3,4.4]]])
print(ar3)
print(type(ar3))
print(ar3.ndim)
#multidimensional array
arn=np.array([1,2,3,4],ndmin=10)
print(arn)
print(arn.ndim)
