import numpy as np
A = np.array([[1, 2],[3, 4]])
print(A)
U,s,VT=np.linalg.svd(A)
print("Left Singular Matrix")
print(U)
print("Singular Matrix")
print(s)
print("Right Singular Matrix")
print(VT)
Sigma = np.zeros((A.shape[0], A.shape[1]))
np.fill_diagonal(Sigma, s)
B = U.dot(Sigma.dot(VT))
print("Reconstructed Matrix:\n",B)



output
=====================
C:\Users\mlm\PycharmProjects\BIBIN\venv\Scripts\python.exe C:\Users\mlm\PycharmProjects\venv\svd.py 
[[1 2]
 [3 4]]
Left Singular Matrix
[[-0.40455358 -0.9145143 ]
 [-0.9145143   0.40455358]]
Singular Matrix
[5.4649857  0.36596619]
Right Singular Matrix
[[-0.57604844 -0.81741556]
 [ 0.81741556 -0.57604844]]
Reconstructed Matrix:
 [[1. 2.]
 [3. 4.]]

Process finished with exit code 0
