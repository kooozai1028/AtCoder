n = int(input())

root_n = int(n ** 0.5)

ans = 0

for i in range(1, root_n + 1):
    if n % i == 0 and i < n // i - 1:
        ans += n // i - 1

print(ans)
