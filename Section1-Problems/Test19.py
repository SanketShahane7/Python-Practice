import numpy as np

A = np.array([1,1,2,2,4])
B = np.array([0.6,1.29,1.99,2.69,3.4])

def mse(A,B):
    '''A,B -> Numpy arrays
       output -> A float rounded up to 2 decimal points should be returned'''
    
    ### STEP 1. Calculate difference between elements of A and B
    diff = A - B
    print("\nDifference between A and B:", diff)

    ## STEP 2: Take square of difference
    sq_diff = diff ** 2
    print("\nSquared difference between A and B:", sq_diff)

    ## STEP3 : Take mean of squared difference
    mean_sq_diff = sq_diff.mean()
    print("\nMean of squared difference between A and B:", mean_sq_diff)
    
    ## STEP 4 : Round off values to 2 decimal places.
    mean_sq_diff = round(mean_sq_diff, 2)
    print("\nMean squared difference rounded to 2 decimal places:", mean_sq_diff)

    return mean_sq_diff


print("\nMean squared error:", mse(A,B))
