# N = 3
# X = 81
# list = [33,105,57]

N,X = map(int,input().split())
list = [int(x) for x in input().split()]
list_dist = sorted([abs(x - X) for x in list])

def gcd(a, b):
    if a < b:
        a , b = b , a
    while b:
        a, b = b, a % b
    return a

ans = list_dist[0]

for x in list_dist[1:]:
    result = gcd(ans,x)

print(result)
