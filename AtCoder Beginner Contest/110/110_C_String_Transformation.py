word1 = input()
word2 = input()

def cnt_element(x):
    dict = {}
    for i in x:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    return  sorted([x for x in dict.values()],reverse=True)

if cnt_element(word1) == cnt_element(word2):
    print('Yes')
else:
    print('No')

#俺の過去回答
# from collections import Counter
#
# S = input()
# T = input()
#
# s = list(Counter(S).values())
# t = list(Counter(T).values())
# s.sort(reverse=True)
# t.sort(reverse=True)
#
# for i,j in zip(s,t):
#     if i != j:
#         print('No')
#         break
# else:
#     print('Yes')

#俺の過去回答
#正解のパターンと不正解のパターンはどうだろう
# S = 'abcdefghijklmnopqrstuvwxyz'
# T = 'ibyhqfrekavclxjstdwgpzmonu'

# S = input()
# T = input()
#
# alphabets = 'abcdefghijklmnopqrstuvwxyz'
#
# S_list = []
# T_list = []
#
# for i in alphabets:
#     Scnt = S.count(i)
#     Tcnt = T.count(i)
#     if Scnt > 0:
#         S_list.append(Scnt)
#     if Tcnt > 0:
#         T_list.append(Tcnt)
#
# if sorted(T_list) == sorted(S_list):
#     print('Yes')
# else:
#     print('No')