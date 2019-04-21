N, M = map(int, input().split())
list = [list(map(int, input().split())) for i in range(N)]

list.sort()
sum = 0
cnt = 0

for A, B in list:
    if cnt + B >= M:
        sum += A * (M - cnt)
        cnt += M - cnt
        break
    sum += A * B
    cnt += B

print(sum)