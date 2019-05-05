N, K = map(int, input().split())
S = input()

l = [0]
curr = '1'

#0と1の塊を探索
for c in S:
    if c != curr:
        l.append(1)
        curr = c
    else:
        l[-1] += 1
if curr == '0':
    l.append(0)

n_group = len(l) // 2
sum_ = 0
k = min(K, n_group)

#初期値として左端から1の塊を算出
for i in range(k):
    sum_ += l[2 * i] + l[2 * i + 1]
sum_ += l[2 * k]
max_ = sum_

#左端から0の塊を１つずつ取り替えて、最大値を算出
for i in range(k, n_group):
    sum_ -= l[2 * i - 2 * K] + l[2 * i + 1 - 2 * K]
    sum_ += l[2 * i + 1] + l[2 * i + 2]
    max_ = max(max_, sum_)

print(max_)
