#各地点の平均気温を算出
#平均気温Aと各地点の平均気温の差分を算出
#平均気温Aとの差分が最も小さい地点を選ぶ

N = int(input())
T,A = map(int,input().split())
H = list(map(int,input().split()))

H_temp = [abs(A-(T-0.006*i)) for i in H]
