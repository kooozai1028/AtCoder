from itertools import product
N = int(input())

cnt = 0
for i in range(3,10):
    for v in product('357',repeat=i):
        val = ''.join(v)
        if int(val) <= N and '3' in val and '5' in val and '7' in val:
           cnt += 1

print(cnt)
