import numpy as np

b = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]])
# b[행, 열]
# print(b[:, 1])
print("x1 = 1,2,3 = {}".format(b[0:1]))
print("x1 = 1,5,9 = {}".format(b[0:1,0:1]))
print("x1 = 1,5,9 = {}".format(b[0:1,0:1]))