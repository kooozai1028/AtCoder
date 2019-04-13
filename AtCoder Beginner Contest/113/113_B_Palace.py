#各地点の平均気温を算出
#平均気温Aと各地点の平均気温の差分を算出
#平均気温Aとの差分が最も小さい地点を選ぶ

N = int(input())
T,A = map(int,input().split())
H = list(map(int,input().split()))

H_temp = [abs(A-(T-0.006*i)) for i in H]

#解答１　解が一意に定まる前提で最小値を探索
for i in range(len(H_temp)):
    if H_temp[i] == min(H_temp):
        print(i+1)

#解答２　最小値書き換え
# temp = 999999
# best_spot = None
#
# for i in range(len(H_temp)):
#     if H_temp[i] < temp:
#         temp = H_temp[i]
#         best_spot = i+1
#
# print(best_spot)