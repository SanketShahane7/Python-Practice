import numpy as np

a = np.array([[ 0,  1,  2,  3],
              [ 4,  5,  6,  7],
              [ 8,  9, 10, 11],
              [12, 13, 14, 15],
              [16, 17, 18, 19]]);

arr = np.array([[3, 3, 8, 2, 2, 1, 3, 9, 2, 3], 
                [7, 9, 9, 7, 2, 2, 2, 7, 0, 5], 
                [5, 1, 1, 9, 4, 7, 0, 4, 4, 8], 
                [1, 3, 7, 2, 1, 1, 2, 0, 4, 3], 
                [6, 4, 4, 4, 2, 5, 7, 3, 9, 6]])

arr1 = np.array([[7, 3, 3, 4, 1, 5, 8, 2, 2, 9], 
                 [9, 0, 9, 7, 2, 6, 9, 3, 8, 1], 
                 [2, 8, 1, 2, 2, 2, 4, 3, 8, 7], 
                 [2, 9, 1, 8, 2, 5, 3, 0, 9, 8], 
                 [0, 6, 5, 1, 1, 6, 1, 6, 1, 6], 
                 [0, 1, 8, 2, 8, 4, 4, 0, 0, 7], 
                 [5, 8, 0, 3, 1, 6, 9, 1, 2, 4], 
                 [9, 2, 9, 8, 7, 5, 2, 5, 7, 3], 
                 [8, 2, 5, 5, 3, 7, 5, 2, 6, 3], 
                 [9, 8, 3, 0, 7, 1, 9, 4, 0, 4]]
)

def extract_subarray(a):
    # 1. return the sub-arry from 2nd row to 4th row
    row_array = a[1:4, :];
    print("--> sub-array: \n", row_array);
    print("\n\n");
    
    # 2. Get the last 3 cols from the row_array
    cols_array = row_array[:, -3:];
    print("--> sub-array: \n", cols_array);
    print("\n\n\n");
    
    
    #3. reverse the rows in cols_array
    result = cols_array[::-1,:];
    print("--> reversed sub-array: \n", result);
    return result;

# extract_subarray(a);
# extract_subarray(arr);
extract_subarray(arr1);
