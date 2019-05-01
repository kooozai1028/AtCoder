from collections import Counter

S = input()
T = input()

s = list(Counter(S).values())
t = list(Counter(T).values())
s.sort(reverse=True)
t.sort(reverse=True)

for i, j in zip(s, t):
    if i != j:
        print('No')
        exit()
else:
    print('Yes')
