N,K = map(int,input().split())

list = [int(input()) for i in range(N)]
list.sort()

print(min(list[i+K-1]-list[i] for i in range(N-K+1)))

#第一回提出
# N,K = map(int,input().split())
#
# list = [int(input()) for i in range(N)]
# list.sort()
# min_val = 10**9
# for i in range(N-K+1):
#     min_val = min(min_val,list[i+K-1]-list[i])
#
# print(min_val)