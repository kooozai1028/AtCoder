import numpy as np

N,M,C = map(int,input().split())
B = list(map(int,input().split()))
cnt = 0

for i in range(N):
    A = list(map(int,input().split()))
    if np.dot(A,B)+C > 0:
        cnt += 1

print(cnt)