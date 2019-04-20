n = 5
a = [6, 8, 1, 2, 3]

a.sort()
print(a)
if n%2 == 0:
    print(2*(sum(a[n//2:])-sum(a[:n//2]))-(a[n//2]-a[n//2-1]))
else:
    print('a[n//2+1:]:'+str(a[n//2+1:]))
    print('a[:n//2]:'+str(a[:n//2]))
    print('a[n//2]:'+str(a[n//2]))
    print('a[n//2+1]:'+str(a[n//2+1]))
    print('a[n//2-1]:'+str(a[n//2-1]))
    print(2*(sum(a[n//2+1:])-sum(a[:n//2]))-min(a[n//2]-a[n//2-1],a[n//2+1]-a[n//2]))

#俺の回答　2018/10/28 Sat

# N = 5
# list = [6, 8, 1, 2, 3]

# N = int(input())
# list = [int(input()) for _ in range(N)]
#
# import itertools
#
# stock = []
#
# for element in itertools.permutations(list):
#     stock_temp = []
#     pre = 0
#     cnt = 0
#     for i in element:
#         if cnt == 0:
#             pre = i
#             cnt += 1
#         else:
#             stock_temp.append(abs(pre - i))
#             pre = i
#             cnt += 1
#     stock.append(sum(stock_temp))
#
# print(max(stock))