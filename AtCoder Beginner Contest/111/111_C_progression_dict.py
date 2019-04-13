n = int(input())
list = [int(i) for i in input().split()]

list_odd = list[::2]
list_even = list[1::2]

def cnt_element(x):
    dict = {}
    for i in x:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    return [(v,k) for k,v in dict.items()]

cnt_odd = sorted(cnt_element(list_odd),reverse=True)
cnt_even = sorted(cnt_element(list_even),reverse=True)

#最頻値が同じの場合
if cnt_odd[0][1] == cnt_even[0][1]:
    #リスト内の値が１つの場合
    if len(cnt_odd) ==1 or len(cnt_even) == 1:
        ans =  int(n / 2)
    #リストが２つ以上の場合
    else:
        #第２最頻値の出現数が奇数の方が多い
        if cnt_odd[1][0] > cnt_even[1][0]:
            ans = n - cnt_odd[1][0] - cnt_even[0][0]
        #第二２最頻値の出現数が偶数の方が多い
        elif cnt_odd[1][0] <= cnt_even[1][0]:
            ans = n - cnt_odd[0][0] - cnt_even[1][0]
#最頻値が異なる場合
else:
    ans = n - cnt_odd[0][0] - cnt_even[0][0]

print(ans)
