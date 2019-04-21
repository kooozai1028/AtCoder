N,M = map(int,input().split())
list = [list(map(int,input().split())) for i in range(N)]
list.sort(key=lambda x:x[0])

def dfs(m,cnt):
    if m <= 0 or cnt == len(list):
        return 0
    b = list[cnt][1] if list[cnt][1] < m else m
    a = b*list[cnt][0]

    return a + dfs(m-b,cnt+1)

print(dfs(M,0))
