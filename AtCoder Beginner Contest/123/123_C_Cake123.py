X,Y,Z,K = map(int,input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

sums = []

for i in range(X):
    for j in range(Y):
        for k in range(Z):
            if (i+1)*(j+1)*(k+1) > K:
                break
            sums.append(A[i]+B[j]+C[k])

for s in sorted(sums,reverse=True)[:K]:
    print(s)
