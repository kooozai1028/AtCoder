#各行の2列目以降を全行で検索し、カウントする
#カウント数がレコード数と一致する場合、格納する
#格納したベクトルの長さが解答
#ただし、レコードが1行の場合はすべての回答数を解答とする

N,M = map(int,input().split())
list = [list(map(int,input().split())) for x in range(N)]

#一列目削除
for i in range(0,N):
    list[i].pop(0)

stock = []

#解答が全リストにあるか探索
for i in range(0,N):
    for j in range(0,len(list[i])):
        cnt = 0
        for k in range(0,N):
            if list[i][j] in list[k]:
                cnt += 1
        if cnt == N:
            stock.append(list[i][j])

if N == 1:
    stock = list[i]

print(len(set(stock)))
