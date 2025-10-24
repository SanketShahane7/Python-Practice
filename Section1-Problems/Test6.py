import numpy as np;
x = np.array([[200,200,200],[300,300,300],[400,400,400]]);
v = np.array([200,300,400]);
print(v[:,None]);
# print(v[:,None][1][1]);
# print((x / v[:,None])[1][1]);


p = np.array([[0],[10],[20]]);
q = np.array([10,11,12]);
print((p+q));
print((p+q)[1][1]);

