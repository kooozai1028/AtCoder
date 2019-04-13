N,K = map(int,input().split())
S = list(input())
print(S)

start = 0
intervals = []
for i in range(1,len(S)):
    if S[start] != S[i]:
        intervals.append((start,i-1,i-1-start+1,S[start]))
        start = i
intervals.append((start,len(S)-1,i-1-start+1,S[start]))

intervals_0 = list(filter(lambda x:x[3]=='0',intervals))
intervals_0.sort(key=lambda x:x[2],reverse=True)
print(intervals_0)
for i in range(K):
    S[intervals_0[i][0]:intervals_0[i][1]+1] = ['1']*(intervals_0[i][1]+1-intervals_0[i][0])
print(S)
max_list = []
cnt_1 = 0

for s in S:
    if s == '1':
        cnt_1 += 1
    else:
        max_list.append(cnt_1)
        cnt_1 = 0

print(max(max_list))