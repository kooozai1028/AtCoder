S = input()
K = int(input())

cnt_1 = 0

for s in S:
    if s == '1':
        cnt_1 += 1
    else:
        break


if K <= cnt_1:
    print(1)
else:
    print(S[cnt_1])
