N,K = map(int,input().split())

#確率の初期値を設定
if N >= K:
    prob = (N-K+1)/N
else:
    prob = 0

#各サイコロの目でコインを振る回数を算出
def count(i,K):
    sum = 0
    cnt = 0
    while sum < K:
        if cnt == 0:
            sum = i*2
            cnt += 1
        else:
            sum = sum*2
            cnt += 1
    return cnt

#NがK-1以下だった場合は1からK-1までのサイコロの目で確率を加算
for i in range(1,N+1):
    if i <= K-1:
        prob += (1/N)*((1/2)**count(i,K))
    else:
        break

print(prob)
