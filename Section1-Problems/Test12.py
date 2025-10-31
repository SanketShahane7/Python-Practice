import numpy as np
arr = np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])

# x = np.hstack((arr,arr[:,0])).shape
x = np.hstack((arr, arr[:, [0]])).shape
print(x)
# output: (3,4)