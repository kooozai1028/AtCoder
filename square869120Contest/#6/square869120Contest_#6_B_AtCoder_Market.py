N = int(input())
list = [list(map(int,input().split())) for _ in range(N)]

in_time = float('inf')
for i in range(N):
    temp = 0
    for j in range(N):
        temp += abs(list[i][0]-list[j][0])
    in_time = min(in_time,temp)

shop_time = 0
for i in range(N):
    shop_time += list[i][1]-list[i][0]

out_time = float('inf')
for i in range(N):
    temp = 0
    for j in range(N):
        temp += abs(list[i][1]-list[j][1])
    out_time = min(out_time,temp)

print(in_time+shop_time+out_time)