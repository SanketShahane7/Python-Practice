import numpy as np
def seq(start, length, step):
    ''' start, length and step are in form of integers all representing the attributes as their names suggest
        output -> A numpy array is expected to be returned'''

    # YOUR CODE GOES HERE and the output array should be 1D array
    sequence = np.arange(start, start + length * step, step)
    sequence = sequence.reshape(-1)
    
    return sequence


x = seq(5, 10, 3)

print(x)  # expected output: [[ 5  8 11 14 17 20 23 26 29 32]]
print(x.shape)  # expected output: (1, 10)
