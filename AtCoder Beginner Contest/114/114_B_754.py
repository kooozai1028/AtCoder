X = input()

ans = 9999
for i in range(len(X)-2):
    ans = min(ans,abs(int(X[i:i+3])-753))

print(ans)