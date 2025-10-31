import numpy as np;

arr1 = np.array([1,2,3,6,3,2]);
arr2 = np.array([4,2,1,3,3,2]);
arr3 = np.zeros(len(arr1));


# which are the one for following are vectorized operations in numpy?
# 1. arr3 = arr1 * arr2
# 2. x = np.where(arr1 > 0, 1, -1)
# 3. for i in range(len(arr1)):
# 4. for i in range(len(arr1)): 
#        if(arr1[i] < 0 ): 
#            arr1[i] = -1 
#        else:
#            arr1[i] = 1
# Answer: 1 and 2 are vectorized operations.


# for i in range(len(arr1)): 
#     arr3[i] = arr1[i] * arr2[i];
# print(arr3);
# # output: [ 4.  4.  3. 18.  9.  4.]

# arr3 = arr1*arr2 
# print(arr3);
# # output: [ 4  4  3 18  9  4]


# for i in range(len(arr1)): 
#     if(arr1[i] < 0 ): 
#         arr1[i] = -1 
#     else: 
#         arr1[i] = 1
# print(arr1);
# # output: [ 1  1  1  1  1  1]


# x = np.where(arr1 > 0, 1, -1)
# print(x);
# # output: [ 1  1  1  1  1  1]




                
