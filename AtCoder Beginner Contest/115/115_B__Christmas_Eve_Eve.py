N = int(input())
list = [int(input()) for i in range(N)]
list.sort(reverse=True)

total = list[0]/2 + sum(list[1:])

print(int(total))

#第一回提出
# N = int(input())
# list = [int(input()) for i in range(N)]
# list.sort(reverse=True)
#
# total = list[0]/2
#
# for i in list[1:]:
#     total += i
#
# print(int(total))