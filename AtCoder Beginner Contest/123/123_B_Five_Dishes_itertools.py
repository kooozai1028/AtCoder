import itertools
list = [int(input()) for _ in range(5)]
temp = 0
ans = 10**9

for v in itertools.permutations(list):
    temp = 0
    for i,j in enumerate(v):
        if i != 4:
            if j % 10 == 0:
                temp += j
            else:
                temp += (j//10+1)*10
        else:
            temp += j
    ans = min(ans,temp)

print(ans)
