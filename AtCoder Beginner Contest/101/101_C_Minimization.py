N,K = map(int,input().split())
list = list(map(int,input().split()))

ans = 1
N = N - K

while N > 0:
    N -= K-1
    ans += 1

print(ans)
