# 1以上 K以下の正の整数から、偶数と奇数ひとつずつの組を選ぶ方法の個数を求めてください。なお、選ぶ順番は考慮しません。

# K = int(input())

from itertools import product

# H, W = map(int, input().split())
# a = [list(map(int, input().split())) for _ in range(H)]

H = 2
W = 3

a = [[1,2,3],[0,1,1]]


output = ''
direction = -1
idou = 0
last_i = 0
last_j = 0
count = 0
j = -1
for i in range(H):
    direction *= -1
    j += direction
    for _ in range(W):
        if idou == 1:
            count += 1
            output += '{} {} {} {}\n'.format(last_i + 1, last_j + 1, i + 1, j + 1)
        if (a[i][j] + idou) % 2 == 1:
            idou = 1
        else:
            idou = 0
        last_i = i
        last_j = j
        j += direction

output = str(count) + '\n' + output.strip()
print(output)