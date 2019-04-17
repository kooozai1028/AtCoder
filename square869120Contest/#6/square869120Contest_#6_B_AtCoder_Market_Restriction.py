N = int(input())
list = [list(map(int,input().split())) for _ in range(N)]

min_val = float('inf')

for en in range(1,100):
    for ex in range(en,101):
        sum = 0
        for l_en,l_ex in list:
            sum += abs(en-l_en)+abs(l_ex-l_en)+abs(l_ex-ex)
        min_val = min(min_val,sum)

print(min_val)
