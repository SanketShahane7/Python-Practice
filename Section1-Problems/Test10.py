import numpy as np;

# What will be the print output of the following code?
# output: A 5x5 array with 1s on the border and 0s in the center
x = np.ones((5,5))
x[1:-1,1:-1] = 0

print(x);
