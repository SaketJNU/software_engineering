import numpy as np
mat = np.zeros([2,2])
print(mat)

mat[0,0] = 2
print(mat)

mat[1,0] = 4
mat[0,1] = 3
mat[1,1] = 5
print(mat)

print("size of matrix elements : ",mat.size) #size of matrix elements
print("Shape of matrix : ",mat.shape) # its for shape of matrix 

help() # for any help ......