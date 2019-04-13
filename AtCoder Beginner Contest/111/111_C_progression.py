n = 12
# v = [33,4,33,4,33,4,33,2,100,101,100,102]
# v = [33,33,33,33,33,33,33,2,100,101,100,102]
v = [115,115,115,115,115,2]

import collections

def answer(list, n):
    Even = collections.Counter(list[::2]).most_common(2)
    Odd = collections.Counter(list[1::2]).most_common(2)

    #最頻値が異なる場合
    if Even[0][0] != Odd[0][0]:
        return n - Even[0][1] - Odd[0][1]
    else:
        #リストの中身が1つの場合
        if len(Even) == 1 or len(Odd) == 1:
            return n // 2
        #最頻値が同じ場合は第２最頻値が少ないほうの値を変換
        else:
            return n - max(Even[0][1] + Odd[1][1], Even[1][1] + Odd[0][1])


N = int(input())
list = input().split(" ")
print(answer(list, N))

#正解　俺の回答

# n = int(input())
# list = [int(i) for i in input().split()]
#
# list_odd = list[::2]
# list_even = list[1::2]
#
# def cnt_element(x):
#     dict = {}
#     for i in x:
#         if i not in dict:
#             dict[i] = 1
#         else:
#             dict[i] += 1
#     return [(v,k) for k,v in dict.items()]
#
# cnt_odd = sorted(cnt_element(list_odd),reverse=True)
# cnt_even = sorted(cnt_element(list_even),reverse=True)
#
# #最頻値が同じの場合
# if cnt_odd[0][1] == cnt_even[0][1]:
#     #リスト内の値が１つの場合
#     if len(cnt_odd) ==1 or len(cnt_even) == 1:
#         ans =  int(n / 2)
#     #リストが２つ以上の場合
#     else:
#         #第２最頻値の出現数が奇数の方が多い
#         if cnt_odd[1][0] > cnt_even[1][0]:
#             ans = n - cnt_odd[1][0] - cnt_even[0][0]
#         #第二２最頻値の出現数が偶数の方が多い
#         elif cnt_odd[1][0] <= cnt_even[1][0]:
#             ans = n - cnt_odd[0][0] - cnt_even[1][0]
# #最頻値が異なる場合
# else:
#     ans = n - cnt_odd[0][0] - cnt_even[0][0]
#
# print(ans)


#模範解答
# from collections import Counter

# n = int(input())
# v = [int(i) for i in input().split()]

# ki = v[::2]
# gu = v[1::2]
#
# ki = Counter(ki)
# gu = Counter(gu)
#
# ki = ki.most_common()
# gu = gu.most_common()
#
# print('ki:'+str(ki))
# print('gu:'+str(gu))
#
# ans = 0
#
# #最頻値が同じ
# if ki[0][0] == gu[0][0]:
#     #リストの値が１つのみ
#     if len(ki) == 1 and len(gu) == 1:
#         ans = int(n / 2)
#     # リストの値が２つ以上
#     else:
#         #第二最頻値が奇数の方が多い場合
#         if ki[1][1] > gu[1][1]:
#             ans = n - ki[1][1] - gu[0][1]
#         #第二最頻値が偶数の方が多い場合
#         else:
#             ans = n - ki[0][1] - gu[1][1]
# #最頻値が異なる
# else:
#     ans = n - ki[0][1] - gu[0][1]
#
# print(ans)


#自分の解答1

# N = int(input())
#num_list = [int(x) for x in input().split()]

#出現する数が２種類かどうか
#一つ置きに値が等しくなっているのか

# num_list = [3,1,3,2]
# count = {}
#
# for i in num_list:
#     if i in count:
#         count[i] += 1
#     else:
#         count[i] = 1
#
# d = [(v,k) for k,v in count.items()]
#
# d.sort()
#
# print(d)

#自分の解答2 10/06

# import collections
# list = [115,115,115,115,115,2]
# n = len(list)
# ans = 0

#両方文字数が1
#　異なる値
#　同じ値
#片方の文字数が1
#　異なる値
#　同じ値
#両方文字数が2以上
#　片方が1文字で片方が2文字以上

# list_odd = list[::2]
# list_even = list[1::2]
#
# def cnt_element(x):
#     dict = {}
#     for i in x:
#         if i not in dict:
#             dict[i] = 1
#         else:
#             dict[i] += 1
#     return [(v,k) for k,v in dict.items()]
#
# cnt_odd = sorted(cnt_element(list_odd),reverse=True)
# cnt_even = sorted(cnt_element(list_even),reverse=True)
# print(cnt_odd)
# print(cnt_even)
#
# if len(cnt_odd) == len(cnt_even) == 1:
#     if cnt_even[0][1] != cnt_odd[0][1]:
#         ans = 0
#     elif cnt_even[0][1] == cnt_odd[0][1]:
#         ans = int(n / 2)
# elif len(cnt_odd) == 1 and len(cnt_even) != 1:
#     ans = n - cnt_odd[0][0] - cnt_even[1][0]
# elif len(cnt_odd) != 1 and len(cnt_even) == 1:
#     ans = n - cnt_even[0][0] - cnt_odd[1][0]
#
# print(ans)