def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

N = int(input())
A = [int(i) for i in input().split()]
X = [0 for i in range(N)]
Y = [0 for i in range(N)]
for i in range(1, N):
    X[i] = gcd(X[i - 1], A[i - 1])
for i in range(N - 1)[::-1]:
    Y[i] = gcd(Y[i + 1], A[i + 1])
Z = [gcd(X[i], Y[i]) for i in range(N)]
print(max(Z))
