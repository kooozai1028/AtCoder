#N+1個分の空リストを用意する
#'AC'が存在する番号に1を付与する
#指定の文字区間でカウントする

N,Q = map(int,input().split())
S = input()

list = [0]*(N+1)

for i in range(N):
    list[i+1] = list[i] + (1 if S[i:i+2] =='AC' else 0)

for i in range(Q):
    l,r = map(int,input().split())
    print(list[r-1]-list[l-1])