N,K = map(int,input().split())

list = [int(input()) for i in range(N)]
list.sort()

print(min(list[i+K-1]-list[i] for i in range(N-K+1)))
