# K = int(input())
K = 3
list = [i for i in range(1, K + 1)]
odd = list[1::2]
even = list[0::2]

cnt = 0

for i in odd:
    for j in even:
        cnt += 1

print(cnt)