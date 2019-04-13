#偶数と奇数の列にわける
#偶数と奇数の列の1と0の数をカウントする

from collections import Counter

S = input()
s_o = S[::2]
s_e = S[1::2]

cnt_o = Counter(s_o).most_common(1)
cnt_e = Counter(s_e).most_common(1)

if len(S) == 1:
    print(0)
else:
    if cnt_o[0][1] >= cnt_e[0][1] and cnt_o[0][0] == '0':
        print(s_o.count('1')+s_e.count('0'))
    elif cnt_o[0][1] >= cnt_e[0][1] and cnt_o[0][0] == '1':
        print(s_o.count('0')+s_e.count('1'))
    elif cnt_o[0][1] < cnt_e[0][1] and cnt_e[0][0] == '0':
        print(s_o.count('0')+s_e.count('1'))
    else:
        print(s_o.count('1')+s_e.count('0'))