N = int(input())
list = [list(map(int,input().split())) for _ in range(N)]
list.sort(key=lambda x:x[1])
 
sum_ = 0
 
for a,b in list:
    sum_ += a
    if sum_ > b:
        print("No")
        exit()
 
print('Yes')
