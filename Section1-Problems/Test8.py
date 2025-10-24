import numpy as np
a = np.array([[16, 5], 
              [81, 6], 
              [33, 1]])
print(np.transpose(a))
print("\n")
print(np.transpose(a).reshape(2,3))
print("\n")
print(np.transpose(a).reshape(3,2))
print("\n")
print(a.flatten())

x=np.transpose(a).reshape(2,3)
print("\n")
print(x.flatten())