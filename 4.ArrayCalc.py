import numpy as np

arr1=np.array([[1,2],[3,4]])
arr2=np.array([[5,6],[7,8]])
print(arr1)
print(arr2)

print("matrix addition")
print(np.add(arr1,arr2))

print("matrix subtraction")
print(np.subtract(arr1,arr2))

print("matrix multiplication of individual elements")
print(np.multiply(arr1,arr2))

print("matrix division")
print(np.divide(arr1,arr2))

print("matrix multiplication")
print(np.dot(arr1,arr2))

print("matrix Transpose")
print(arr1.transpose())

print("Sum of diagonal elements of matrix")
print(np.trace(arr1))



   RESULT
   ------

   C:\Users\mlm\PycharmProjects\pythonProject\venv\Scripts\python.exe C:\Users\mlm\PycharmProjects\pythonProject\venv\arraycalc.py 
[[1 2]
 [3 4]]
[[5 6]
 [7 8]]
matrix addition
[[ 6  8]
 [10 12]]
matrix subtraction
[[-4 -4]
 [-4 -4]]
matrix multiplication of individual elements
[[ 5 12]
 [21 32]]
matrix division
[[0.2        0.33333333]
 [0.42857143 0.5       ]]
matrix multiplication
[[19 22]
 [43 50]]
matrix Transpose
[[1 3]
 [2 4]]
Sum of diagonal elements of matrix
5

Process finished with exit code 0
