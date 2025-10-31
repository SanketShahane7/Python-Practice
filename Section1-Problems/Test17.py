import numpy as np;

A = np.array([2, 0, 1, 9, 1, 1, 1, 0, 3, 5])
# How can add 1 to each element of array A
B = A + 1

print("Array after adding 1:", B)

print("\nArray after adding 1:", [x+1 for x in A])

print("\nArray after adding 1:", list(map(lambda x:x+1, A)))