#負の値をカウントする
#もし負の値が偶数の場合
##合計を算出
#もし負の値が奇数の場合
##最大の負の値を除く

N = int(input())
list = list(map(int,input().split()))
list.sort()

cnt_min = len([i for i in list if i < 0])
num_min = min([abs(i) for i in list])
sum_abs = sum([abs(i) for i in list])

if cnt_min%2 == 0:
    print(sum_abs)
else:
    print(sum_abs-2*num_min)
