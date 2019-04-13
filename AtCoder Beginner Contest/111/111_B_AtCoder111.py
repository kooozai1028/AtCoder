# N = int(input())
N = 112
repdigit = [str(x)*3 for x in range(1,10)]

for i in range(len(repdigit)):
    try:
        if N <= int(repdigit[i]):
            print(repdigit[i])
            break
    except:
        pass


# 解答例
# t = 111
# n = int(input())
# while t < n:
#     t += 111
# print(t)