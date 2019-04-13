list = list(map(int,input().split()))
list.sort(reverse=True)

if list[0]-1 >= list[1]:
    print(list[0]*2-1)
else:
    print(list[0]+list[1])