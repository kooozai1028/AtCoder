# 整数 N,Kが与えられます。N以下の正の整数の組 (a,b,c)であって、
# a+b,b+c,c+aがすべてKの倍数であるようなものの個数を求めてください。
# ただし、a,b,cの順番を入れ替えただけの組も異なるものとして数えます。
# また、a,b,cの中に同じものがあっても構いません。

#1 N以下の正の整数の組み合わせを求める
#2 a+b,b+c,c+aがすべて Kの倍数であるか確認する
#3 Kの倍数であれば格納

# n = 3
# k = 2

n,k = map(int,input().split())

if k%2==1:
    ans = (n//k)**3
else:
    even = n//k
    odd  = (2*n)//k - even
    ans = even**3 + odd**3
print(ans)

# ↓俺の答え

# N,K = map(int, input().split())
#
# cnt = 0
# ans = []
#
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         for k in range(1,N+1):
#             if (i + j) % K == 0 and (j + k) % K == 0 and (k + i) % K == 0:
#                 cnt += 1
#                 ans.append([i,j,k])
# print(cnt)
