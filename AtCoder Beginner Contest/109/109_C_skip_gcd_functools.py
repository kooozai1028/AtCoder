import functools
N,X = map(int,input().split())
list = list(map(int,input().split()))
diff_x = [abs(X-i) for i in list]

def gcd(a,b):
    while b:
        a,b = b,a%b
    return a

print(functools.reduce(gcd,diff_x))
