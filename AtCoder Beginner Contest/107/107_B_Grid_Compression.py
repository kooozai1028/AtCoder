# h, w = map(int, input().split())

# A = []
# for i in range(h):
#     A.append(input())

h = 4
w = 4

A = ['##.#', '....', '##.#', '.#.#']

H = [0 for i in range(h)]
W = [0 for i in range(w)]

for i in range(h):
    if A[i] == "." * w:
        H[i] = 1

for i in range(w):
    co = 0
    for j in range(h):
        print(A[j][i])
        if A[j][i] == ".":
            co += 1
    if co == h:
        W[i] = 1

B = []

for i in range(h):
    st = ""
    if H[i] == 0:
        for j in range(w):
            if W[j] == 0:
                st += A[i][j]
        print(st)

#俺の解答

#'.'のみの行、列の判定方法がわからない
#'.'のみの行、列の削除方法がわからない

# grid = [['#','#','.','#'],['.','.','.','.'],['#','#','.','#'],['.','#','.','#']]
#
# for i in range(len(grid)):
#     for j in grid[i]:
#         print(j)
#
#
# print(grid)

#俺の解答 9/29

# matrix = ['##.#','....','##.#','.#.#']
# ans = []
# row = []
# col = []
#
# for i in matrix:
#     cnt = 0
#     cnt_dot = 0
#     #行の確認
#     for j in i:
#         cnt += 1
#         if j == '.':
#             cnt_dot += 1
#     #列の確認
#     if cnt == cnt_dot:
#         row.append(1)
#     else:
#         row.append(0)
#
# print(row)
#
# for i in range(len(matrix)):
#     if row[i] == 0:
#         ans.append(matrix[i])
#
# for i in ans:
#     print(i)

#俺の解答 10/8
# H = 4
# W = 4
# list = ['##.#', '....', '##.#', '.#.#']
# # list = ['.....', '.....', '..#..', '.....']
#
# H, W = map(int, input().split())
# list = []
# for i in range(H):
#     list.append(input())
#
# new_list = []
#
# H_del = []
# W_del = []
#
# #削除する行列の探索
# for i in range(H):
#     if list[i] == '.'*W:
#         W_del.append(i)
#
# for i in range(W):
#     H_stock = ''
#     for j in range(H):
#         H_stock += list[j][i]
#         if H_stock == '.'*H:
#             H_del.append(i)
#
# #削除する行列を除いた行列を再作成
# for i in range(H):
#     if i not in W_del:
#         W_list = ''
#         for j in range(W):
#             if j not in H_del:
#                 W_list += list[i][j]
#         new_list.append(W_list)
#
# #答えを表示
# for i in range(len(new_list)):
#     print(new_list[i])