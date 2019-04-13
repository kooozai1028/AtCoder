#模範解答
#質問の全量をリストとして格納
#各行に質問リストの項目が存在するか確認し、あれば残す
#最終的に残っていた項目が解答

N,M = map(int,input().split())
res = set(range(1,M+1))
print(res)

for i in range(N):
    a,*b = map(int,input().split())
    res &= set(b)

print(len(res))

#最終提出
#各行の2列目以降を全行で検索し、カウントする
#カウント数がレコード数と一致する場合、格納する
#格納したベクトルの長さが解答
#ただし、レコードが1行の場合はすべての回答数を解答とする

# N,M = map(int,input().split())
# list = [list(map(int,input().split())) for x in range(N)]
#
# #一列目削除
# for i in range(0,N):
#     list[i].pop(0)
#
# stock = []
#
# #解答が全リストにあるか探索
# for i in range(0,N):
#     for j in range(0,len(list[i])):
#         cnt = 0
#         for k in range(0,N):
#             if list[i][j] in list[k]:
#                 cnt += 1
#         if cnt == N:
#             stock.append(list[i][j])
#
# if N == 1:
#     stock = list[i]
#
# print(len(set(stock)))


#一回目提出
# N,M = map(int,input().split())
# list = [list(map(int,input().split())) for x in range(N)]
#
# #一列目削除
# for i in range(0,N):
#     list[i].pop(0)
#
# stock = []
#
# #解答が全リストにあるか探索
# for i in range(0,N):
#     cnt = 0
#     for j in range(0,len(list[i])):
#         print('list[i][j]:'+str(list[i][j]))
#         print('list[i]:'+str(list[i]))
#         if list[i][j] in list[i]:
#             cnt += 1
#         print('cnt:'+str(cnt))
#     if cnt == N:
#         stock.append(list[i][j])
#
# if N == 1:
#     stock = list[i]
#
# print(len(stock))