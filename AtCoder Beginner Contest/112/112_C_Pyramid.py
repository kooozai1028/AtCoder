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


#模範解答１
# x0, y0, h0 = 0, 0, 0
#
# #hが0でない組をサンプルとして代入
# for i in range(N):
#     if list[i][2]:
#         x0, y0, h0 = list[i]
#
# #cxとcyの全組み合わせを実装
# for cx in range(0, 101):
#     for cy in range(0, 101):
#         # H候補を洗い出し
#         H = h0 + abs(x0 - cx) + abs(y0 - cy)
#         f = False
#         # もしhが異なるなら不正解
#         for x, y, h in l:
#             if h != max(H - abs(x - cx) - abs(y - cy), 0):
#                 print(h,max(H - abs(x - cx) - abs(y - cy), 0))
#                 f = True
#                 break
#         #　hが一致するときのcx,cy,Hの値を出力
#         if not f:
#             print(cx, cy, H)

#模範解答２
# coords = [[2, 3, 5], [2, 1, 5], [1, 2, 5], [3, 2, 5]]
#
# # 全探索
# def search():
#     for Cx in range(101):
#         for Cy in range(101):
#             x, y, h = tuple(coords[0])
#             H = h + abs(Cx - x) + abs(Cy - y)
#             for x, y, h in coords:
#                 if max(H - abs(Cx - x) - abs(Cy - y), 0) != h:
#                     break
#             else:
#                 return Cx, Cy, H
#
#
# x, y, h = search()
# print("{} {} {}".format(x, y, h))


# 俺の解答
# list = [[0,0,100],[1,1,98]]
# 
# H_stock = []
# dict = {}
# 
# for i in range(len(list)):
#     for x in range(0,101):
#         for y in range(0,101):
#             # H = [list[i][2],abs(list[i][0]-x),abs(list[i][1]-y)]
#             H = str(list[i][2])+','+str(abs(list[i][0]-x))+','+str(abs(list[i][1]-y))
#             if H not in dict:
#                 dict[H] = 1
#             else:
#                 dict[H] += 1
# 
# print(sorted(dict,reverse=True))
