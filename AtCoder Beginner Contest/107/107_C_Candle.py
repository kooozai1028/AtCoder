n, k = map(int, input().split())
x = list(map(int, input().split()))

ans = 10 ** 9

for i in range(n - k + 1):
    if x[i] >= 0:
        ans = min(ans, x[i + k - 1])
    elif x[k + i - 1] <= 0:
        ans = min(ans, -x[i])
    else:
        ans = min(ans, x[k + i - 1] * 2 - x[i], x[k + i - 1] - x[i] * 2)

print(ans)

#俺の回答 2019/04/08

# N,K = map(int,input().split())
# list = list(map(int,input().split()))
# ans = 10**9
#
# for i in range(N-K+1):
#     temp = 0
#     if list[i] > 0:
#         temp = list[i+K-1]
#     elif list[i+K-1] < 0:
#         temp = abs(list[i])
#     else:
#         temp = list[i+K-1]+abs(list[i])+min(list[i+K-1],abs(list[i]))
#
#     ans = min(ans,temp)
#
# print(ans)

#俺の回答 2018/10/21

# K本のろうそくを点灯するまで最小距離を計算する。ただし、初期値は0

# N,K = map(int,input().split())
# list = list(map(int,input().split()))
#
# def calc_dist(list,current):
#     min_dist = 0
#     next_point = 0
#     for i in list:
#         dist = abs(i-current)
#         print(dist)
#         if dist < min_dist:
#             min_dist = dist
#             next_point = i
#
#     return next_point
#
# print(calc_dist(list,0))