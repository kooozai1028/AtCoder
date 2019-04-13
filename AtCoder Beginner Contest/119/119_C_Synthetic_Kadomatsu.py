N,A,B,C = map(int,input().split())
l = [int(input()) for i in range(N)]

def dfs(cur,a,b,c):
    if cur == N:
        return abs(a-A) + abs(b-B) + abs(c-C) - 30 if min(a,b,c) > 0 else 10**9
    ret0 = dfs(cur+1,a,b,c)
    ret1 = dfs(cur+1,a+l[cur],b,c) + (10 if a != 0 else 0)
    ret2 = dfs(cur+1,a,b+l[cur],c) + (10 if b != 0 else 0)
    ret3 = dfs(cur+1,a,b,c+l[cur]) + (10 if c != 0 else 0)
    return min(ret0,ret1,ret2,ret3)

print(dfs(0,0,0,0))
