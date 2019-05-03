import sys
sys.setrecursionlimit(10**6)

N = int(input())
S = input()

result = S.count('.')
r = result
def dfs(i):
    global result
    global r
    if i == N:
        return float('inf')
    if S[i] == '#':
        r += 1
    else:
        r -= 1
    result = min(result,r)
    return min(result,dfs(i+1))

print(dfs(0))
