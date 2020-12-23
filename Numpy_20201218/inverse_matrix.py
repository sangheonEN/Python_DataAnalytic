# 단위행렬 (Unit matrix): np.eye(n)
# 대각행렬 (Diagonal matrix): np.diag(x)
# 내적 (Dot product, Inner product): np.dot(a, b)
# 대각합 (Trace): np.trace(x)
# 행렬식 (Matrix Determinant): np.linalg.det(x)
# 역행렬 (Inverse of a matrix): np.linalg.inv(x)
# 고유값 (Eigenvalue), 고유벡터 (Eigenvector): w, v = np.linalg.eig(x)
# 특이값 분해 (Singular Value Decomposition): u, s, vh = np.linalg.svd(A)
# 연립방정식 해 풀기 (Solve a linear matrix equation): np.linalg.solve(a, b)
# 최소자승 해 풀기 (Compute the Least-squares solution): m, c = np.linalg.lstsq(A, y, rcond=None)[0]

import numpy as np

# 단위 행렬 np.eye(shape=?)
print("단위 행렬")
unit_matrix = np.eye(4)
print(unit_matrix)

# 대각 행렬 np.diag()    대각 원소 빼고 전부 0으로 만듬
print("대각 행렬")
matrix = np.arange(9).reshape(3,3)
print(f"대각 행렬 변경 전 {matrix}")
diagonal_matrix = np.diag(matrix)
print(f"대각 행렬 변경 후 {diagonal_matrix}")

# 대각합
a = np.trace(matrix)
print(f"대각 행렬 원소 합 = {a}")

# 행렬식 역행렬이 존재하는지 안하는지 확인 출력 값이 0 이면 역행렬 존재 하지 않음
matrix2 = np.arange(4).reshape(2,2)
matrix3 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [0, 0, 0]])
b = np.linalg.det(matrix2)
c = np.linalg.det(matrix3)
print(f"행렬식 b = {b}, c = {c}")

# 역행렬 구하기.np.linalg.inv(x)
matrix4 = np.linalg.inv(matrix2)
print(f" 1 = {matrix2} 의 1번 역행렬 = {matrix4}")

# 