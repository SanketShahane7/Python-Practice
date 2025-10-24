import numpy as np

arr = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
]);

def rotate_array(arr):
    print("--> origional array: \n", arr);
    # return arr[:1,:2];
    # return arr[::-1];
    return arr[::-1].T;

rotated = rotate_array(arr);
print("--> rotated array: \n", rotated);
