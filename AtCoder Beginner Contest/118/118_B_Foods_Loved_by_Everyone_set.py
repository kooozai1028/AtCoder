#質問の全量をリストとして格納
#各行に質問リストの項目が存在するか確認し、あれば残す
#最終的に残っていた項目が解答

N,M = map(int,input().split())
res = set(range(1,M+1))

for i in range(N):
    a,*b = map(int,input().split())
    res &= set(b)

print(len(res))
