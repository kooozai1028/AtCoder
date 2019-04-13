list = [int(input()) for _ in range(5)]
k = int(input())

if max(list) - min(list) > k:
    print(':(')
else:
    print('Yay!')
