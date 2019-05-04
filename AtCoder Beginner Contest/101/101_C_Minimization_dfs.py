import sys
sys.setrecursionlimit(10**6)

N,K = map(int,input().split())
list = list(map(int,input().split()))

def dfs(N,ans):
    if N <= 0:
        return ans
    return dfs(N-(K -1),ans+1)

print(dfs(N-K,1))
