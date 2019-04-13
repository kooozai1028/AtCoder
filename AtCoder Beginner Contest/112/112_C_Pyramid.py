#高さが0でない初期値を設定
#Cx,Cyを全Nパターンで全検索
#初期値から一意に定まる仮Hを算出
#仮HとCx,Cyと一致するhを求め、一致したときのCx,Cy,Hを求める

N = int(input())
list = [list(map(int,input().split())) for x in range(N)]

x0, y0, h0 = 0, 0, 0

#hが0以上である条件を満たす組でHを求める
for i in range(N):
    if list[i][2]:
        x0, y0, h0 = list[i]

for Cx in range(101):
    for Cy in range(101):
        H = h0 + abs(x0 - Cx) + abs(y0 - Cy)
        for i in range(len(list)):
            if list[i][2] != max(H-abs(list[i][0]-Cx)-abs(list[i][1]-Cy),0):
                break
        else:
            print(Cx,Cy,H)
