N,T = map(int,input().split())
list = list(map(int,input().split()))

print(sum(list)//T + (1 if sum(list)%T != 0 else 0))
