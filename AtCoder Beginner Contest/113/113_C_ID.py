#同一県で識別するために空のリストを作成する
#同一県の市を市の番号ともとの並び順を保持したままリストに格納する
#答えの空リストを作成する
#同一県でソートし、市の番号を振る
#もとの順番で県番号と子番号を0埋めした値を答えに格納

N,M = map(int,input().split())
list = [[] for i in range(N)]

for i in range(M):
    p,y = map(int,input().split())
    list[p-1].append((y,i))

ans = [None]*M

for j,list_p in enumerate(list):
    list_p.sort()
    for k,(p,y) in enumerate(list_p):
        ans[y] = '%06d%06d' % (j+1,k+1)

print(*ans,sep='\n')
