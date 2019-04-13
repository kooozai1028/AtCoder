# A = 9
# B = 9
# C = 9

A,B,C = map(int, input().split())

num = sorted([A,B,C],reverse=True)
print(eval(str(num[0])+str(num[1])+'+'+str(num[2])))