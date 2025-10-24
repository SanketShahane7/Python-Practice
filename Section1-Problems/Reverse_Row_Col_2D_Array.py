import numpy as np

arr = np.array([[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15]])

def reverse_column(arr):
    '''
    INPUT: arr -> 2D array 
    OUTPUT rev_arr -> 2D array
    '''
    
    rev_arr = arr[:,::-1]
    
    return rev_arr


def reverse_row(arr):
    '''
    INPUT: arr -> 2D array 
    OUTPUT rev_arr -> 2D array
    '''
    
    rev_arr = arr[::-1,:]
    
    return rev_arr


print(reverse_column(arr))
print("\n")
print(reverse_row(arr))