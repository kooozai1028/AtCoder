N,T = map(int,input().split())
list = [list(map(int,input().split())) for _ in range(N)]
min_cost = list[0][0]
cnt = 0

for c,t in list:
    if t <= T:
        cnt += 1
        comp_cost = c
        if comp_cost < min_cost:
            min_cost = comp_cost

if cnt >= 1:
    print(min_cost)
elif cnt == 0:
    print('TLE')
