N, M = map(int, input().split())
MOD = 10 ** 9 + 7

arrs = set([int(input()) for _ in range(M)])
anss = [0, 1]
for i in range(1, N + 1):
    if i in arrs:
        anss.append(0)
    else:
        anss.append((anss[-2] + anss[-1]) % MOD)

print(anss[-1] % MOD)
