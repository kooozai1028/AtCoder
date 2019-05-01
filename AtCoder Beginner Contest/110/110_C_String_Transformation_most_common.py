from collections import Counter

S = input()
T = input()

S_cnt = Counter(S).most_common()
T_cnt = Counter(T).most_common()

if len(S_cnt) != len(T_cnt):
    print('No')
else:
    for i in range(len(S_cnt)):
        if S_cnt[i][1] != T_cnt[i][1]:
            print('No')
            exit()
    print('Yes')
