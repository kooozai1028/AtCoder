# N, T = map(int, input().split())
# list = [list(map(int, input().split())) for _ in range(N)]

# N = 3
# T = 70
# list = [[7, 60], [1, 80], [4, 50]]

N = 4
T = 3
list = [[1, 1000], [2, 4], [3, 1000],[4, 500]]

cost_list = []

for i in range(len(list)):
    if list[i][1] <= T:
        cost_list.append(list[i][0])

if len(cost_list) >= 1:
    print(min(cost_list))
elif len(cost_list) == 0:
    print('TLE')

#解答2

# N,T = map(int,input().split())
# list = [list(map(int,input().split())) for _ in range(N)]
# min_cost = list[0][0]
# cnt = 0
#
# for c,t in list:
#     if t <= T:
#         cnt += 1
#         comp_cost = c
#         if comp_cost < min_cost:
#             min_cost = comp_cost
#
# if cnt >= 1:
#     print(min_cost)
# elif cnt == 0:
#     print('TLE')