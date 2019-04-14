from math import ceil

D, G = [int(t) for t in input().split()]
p = []
c = []
for i in range(D):
    p_, c_ = [int(t) for t in input().split()]
    p.append(p_)
    c.append(c_)

def solve(G, i):
    """100i点以下の問題だけでGを達成する最小問題数"""
    if i <= 0:
        return float('inf')
    #最も配転が高い問題で総合点を超えることができるか確認
    n = min(ceil(G / (100 * i)), p[i - 1])
    s = 100 * i * n
    #もし総合展を超えることができるときの問題数がボーナス点に達するならば足す
    if n == p[i - 1]:
        s += c[i - 1]
    if G > s:
        n += solve(G - s, i - 1)
    return min(n, solve(G, i - 1))

print(solve(G, D))