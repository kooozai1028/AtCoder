def f(x):
    if x % 4 == 1:
        return 1
    elif x % 4 == 2:
        return a + 1
    elif x % 4 == 3 or x == 0:
        return 0
    else:
        return x


a, b = map(int, input().split())
print(f(b) ^ f(a - 1))
