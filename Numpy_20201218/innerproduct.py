# 벡터의 내적 : 각 원소 순서에 맞추어 곱한 값의 합. x = x1, x2 x3 y = y1, y2, y3  x 내적 y = x1y1 + x2y2 + x3y3
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3])
y = np.array([3, 4, 5])

# dot()함수 사용
print(f"1차원 내적 계산\nx = {x}, y = {y}")
print(f"x내적y = {x.dot(y)}")
print(f"y내적x = {y.dot(x)}")

x1= np.arange(4).reshape(2,2)
y1= np.arange(4).reshape(2,2)
print(f"2차원 내적 계산\nx = {x1}, \ny = {y1}")
print(f"x내적y = {x1.dot(y1)}")
print(f"y내적x = {y1.dot(x1)}")

print("shape이 다른 행렬 내적 연산 2 * 3 행렬과 3 * 2 행렬")
x2 = np.arange(6).reshape(2,3)
y2 = np.arange(6).reshape(3,2)
print(f"x = {x2},\ny = {y2}")
print(f"내적 계산 x내적y = {x2.dot(y2)}")
print(f"내적 계산 y내적x = {y2.dot(x2)}")

# # 정사영 모델링 x = (2, -1, 3), y = (4, -1, 2)
# x3 = np.array([2, -1, 3])
# y3 = np.array([4, -1, 2])
# xy = x.dot(y)
# xx = x.dot(x)
# k = xy/xx
# proj_y = k*x3
# w = y - proj_y
# print(f"x 위로의 y의 정사영 proj_y와 x에 수직인 y의 벡터성분 w를 구해라. ")
# print(f"정사영 proj_y = {proj_y.round(2)}, w = {w.round(2)}")

# 정사영을 이용한 어느 한 점에서 하나의 평면까지의 최단 거리를 구해보자.
# 평면 = x+3y-2z-6 = 0, 어느 한 점 P = (3, -1, 2)
print("정사영을 이용한 한 점에서 하나의 평면까지의 최단거리")
n = np.array([1, 3, -2])
V = np.array([3, -1, 2])
d = -6
VN = V.dot(n)
NN = np.linalg.norm(n, axis=0, ord=2)
D = np.abs(VN+d)/NN
print(f"D = {round(D, 2)}")




