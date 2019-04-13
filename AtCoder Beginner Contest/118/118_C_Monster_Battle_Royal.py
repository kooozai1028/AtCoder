N = int(input())
A = list(map(int, input().split()))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

gcd_val = A[0]
for a in A[1:]:
    gcd_val = gcd(gcd_val, a)
print(gcd_val)