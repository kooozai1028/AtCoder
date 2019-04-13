#偶数列と奇数列にわける
#最頻値と第二最頻値を求める
#最頻値が同じ
#  長さが1
#  長さが2以上
#最頻値が異なる

from collections import Counter
n = int(input())
list = list(map(int,input().split()))
list_o = list[::2]
list_e = list[1::2]

cnt_o = Counter(list_e).most_common(2)
cnt_e = Counter(list_o).most_common(2)

if cnt_o[0][0] == cnt_e[0][0]:
    if len(cnt_o) == 1 and len(cnt_e) == 1:
        print(int(n/2))
    else:
        print(n-cnt_o[0][1]-max(cnt_o[1][1],cnt_e[1][1]))
else:
    print(n-cnt_o[0][1]-cnt_e[0][1])
