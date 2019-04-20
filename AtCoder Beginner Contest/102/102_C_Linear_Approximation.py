#Aiとのiの差分リストを取得
#差分リストから中央値を取得
#abs関数で最小値を算出

N = int(input())
list = list(map(int,input().split()))
diff = [list[i]-(i+1) for i in range(N)]
diff.sort()

m = diff[len(diff)//2]
ans = 0

for i,l in enumerate(list):
    ans += abs(list[i]-(i+1+m))

print(ans)