# 1以上3以下の整数 A,B が与えられます。A×B×C が奇数となるような 1 以上 3 以下の整数 C が存在するか判定してください。

A, B = map(int, input().split())

if A * B % 2 == 1:
    print('Yes')
else:
    print('No')