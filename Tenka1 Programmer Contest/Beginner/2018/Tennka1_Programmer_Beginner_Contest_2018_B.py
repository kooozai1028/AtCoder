# A,B,K = 5,4,2

# もし奇数なら-1して2で割る
# 割った値を相手に渡す
# K回繰り返す

A,B,K = map(int,input().split())

def give_cookie(x,y):
    if x % 2 != 0:
        x -= 1
    x /= 2
    y += x
    return x,y

for i in range(K):
    if i % 2 == 0:
        A,B = give_cookie(A,B)
    else:
        B,A = give_cookie(B,A)

print(int(A),int(B))