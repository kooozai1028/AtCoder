N = int(input())
S = [input() for _ in range(N)]
 
ans = 0
b_start = 0
a_end = 0
b_start_and_a_end = 0
for s in S:
    ans += s.count("AB")
    if s[0] == "B" and s[-1] == "A":
        b_start_and_a_end += 1
    elif s[0] == "B":
        b_start += 1
    elif s[-1] == "A":
        a_end += 1
 
ans += min(b_start, a_end)
 
if b_start == 0 and a_end == 0:
    ans += max(0, b_start_and_a_end - 1)
else:
    ans += b_start_and_a_end
 
print(ans)
