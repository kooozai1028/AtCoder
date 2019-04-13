#一文字ずつ取り出す
#もしacgtならばカウントに１を足す
#もしそうでないならばカウントをゼロにする
#最大値をとる

cnt = 0
list = []
for i in input():
    if i in ['A','C','G','T']:
        cnt += 1
    else:
        if cnt >= 1:
            list.append(cnt)
        cnt = 0

list.append(cnt)

print(max(list) if list else 0)