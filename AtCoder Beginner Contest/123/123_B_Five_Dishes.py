list = [int(input()) for _ in range(5)]
list_diff = []

for i in list:
    if i%10 == 0:
        list_diff.append([0,i,i])
    else:
        list_diff.append([10-i%10,i,10*(i//10+1)])

list_diff.sort()
ans = 0

for i in range(5):
    if i == 4:
        ans += list_diff[i][1]
    else:
        ans += list_diff[i][2]

print(ans)

# import itertools
# list = [int(input()) for _ in range(5)]
# temp = 0
# ans = 10**9
#
# for v in itertools.permutations(list):
#     temp = 0
#     for i,j in enumerate(v):
#         if i != 4:
#             if j % 10 == 0:
#                 temp += j
#             else:
#                 temp += (j//10+1)*10
#         else:
#             temp += j
#     ans = min(ans,temp)
#
# print(ans)