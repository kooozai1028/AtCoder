N = int(input())
list = [int(input()) for _ in range(5)]

min_val = min(list)

if N%min_val == 0:
    print(N//min_val+4)
else:
    print(N//min_val+4+1)
