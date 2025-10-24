import numpy as np

def get_elements(arr):
    '''
    INPUT: arr -> 1D numpy array
    OUTPUT elements -> tuple of first and last element.
    '''

    first_element = int(arr[0])

    last_element = int(arr[-1])
    return (first_element, last_element)

print(get_elements(np.array([0,1,2,3,4,5])))