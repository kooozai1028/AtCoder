list = [int(input()) for _ in range(5)]
list_diff = []

for i in list:
    if i%10 == 0:
        list_diff.append([0,i,i])
    else:
        list_diff.append([10-i%10,i,10*(i//10+1)])

list_diff.sort()
ans = 0

for i in range(5):
    if i == 4:
        ans += list_diff[i][1]
    else:
        ans += list_diff[i][2]

print(ans)
