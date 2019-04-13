N,M = map(int,input().split())
list = list(map(int,input().split()))
list.sort()

diff = [b-a for a,b in zip(list,list[1::])]
diff.sort(reverse=True)
print(sum(diff[N-1:]) if M-N >0 else 0)