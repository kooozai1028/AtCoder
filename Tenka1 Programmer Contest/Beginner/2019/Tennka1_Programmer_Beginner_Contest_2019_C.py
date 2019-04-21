N = int(input())
S = input()

r = S.count(".")
result = r
for i in range(N):
    if S[i] == "#":
        r += 1
    else:
        r -= 1
    result = min(result, r)
    print(result,r)

print(result)

# N = int(input())
# S = input()
# list = [0]*N
#
# for i in range(N-1):
#     if S[i:i+2] == '#.' and (S[:i-1].count('.') == len(S[:i-1]) or (S[:i-1].count('.')+list[:i-1].count(1) == len(S[:i-1]))):
#         list[i] = 1
#     elif S[i:i+2] == '#.':
#         list[i+1] = 2
#
# for i in range(N-1):
#     if list[i] == 2 and S[i+1] == '.':
#         list[i+1] = 2
#
# print(list.count(1)+list.count(2))