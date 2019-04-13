s = int(input())

list = []

while s not in list:
    list.append(s)
    if s % 2 == 0:
        s //=  2
    else:
        s = 3*s + 1

print(len(list)+1)

#初回提出
# s = int(input())
#
# cnt = 1
# list = []
# list.append(s)
# while True:
#     if s % 2 == 0:
#         s = int(s/2)
#     else:
#         s = 3*s + 1
#     cnt += 1
#     if s in list:
#         break
#     list.append(s)
#
# print(cnt)