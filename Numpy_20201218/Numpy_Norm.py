# norm()
import numpy as np
a = [2, -1, 3, 2]
b = [3, 2, 1, -4]

# 1차원 벡터 노름 연산
X = np.array(a)
Y = np.array(b)

# X, Y의 NORM을 구해라. 값의 사이 거리
# 원점과 X의 사이 거리.
# if) ord = 1 -> 거리 누적 합 절대값 계산, ord = 2 -> 거리 누적 피타고리스 정의. 두 점의 차이 값에 제곱 누적합을 루트로 나누어줌.
# if) axis = 0 행 기준
print("1차원 벡터 노름 연산")
print(f"X = {X},\nY = {Y}")
X_norm = np.linalg.norm(X, axis=0, ord=2)
Y_norm = np.linalg.norm(Y, axis=0, ord=2)
XY_norm = np.linalg.norm(X-Y, axis=0, ord=2)
print(f"||X|| = {round(X_norm, 2)}")
print(f"||Y|| = {round(Y_norm, 2)}")
print(f"||X-Y|| = {round(XY_norm, 2)}")

# 2차원 벡터 노름 연산 # axis = 0 : 열 방향으로 x1,x2 연산시작, axis = 1 : 행 방향으로 x1, x2 연산시작
# X_list = np.arange(9).reshape(3,3)
# Y_list = np.arange(9, 18).reshape(3,3)
# X_list = np.random.randint(0,2,(2,2), dtype=int)
# Y_list = np.random.randint(0,2,(2,2), dtype=int)
print("2차원 벡터 노름 연산")
list = [1, 2, 3, 4]
X_list = np.array(list).reshape(2,2)
Y_list = np.array(list).reshape(2,2)
print(f"X = {X_list},\nY = {Y_list}")
X_norm1 = np.linalg.norm(X_list, axis=1, ord=2)
X_norm0 = np.linalg.norm(X_list, axis=0, ord=2)
print(f"X_norm1 행방향 연산 = {X_norm1.round(2)},\nX_norm0 열방향 연산 = {X_norm0.round(2)}")
Y_norm1 = np.linalg.norm(Y_list, axis=1, ord=2)
Y_norm0 = np.linalg.norm(Y_list, axis=0, ord=2)
print(f"Y_norm1 행방향 연산 = {Y_norm1.round(2)},\nY_norm0 열방향 연산 = {Y_norm0.round(2)}")