A,B,K = map(int,input().split())

list = []
for i in range(1,101):
    if A % i == 0 and B % i == 0:
        list.append(i)

list.sort(reverse=True)
print(list[K-1])