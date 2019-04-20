N = int(input())
list = list(map(int,input().split()))

ans = 0
for l in list:
    ans += l-1

print(ans)