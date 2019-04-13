N = 4
M = 2
X = -48
Y = -1
x = [-20,-35,-91,-23]
y = [-22,66]

N,M,X,Y = map(int, input().split())
num_list = [list(map(int, input().split())) for _ in range(2)]

Z = list(range(X+1,Y+1))

for z in Z:
    if max(num_list[0]) < z and min(num_list[1]) >= z:
        print('No War')
        break
    if z == Z[-1]:
        print('War')

#自分の回答

# N, M, X, Y = map(int, input().split())
# num_list = [list(map(int, input().split())) for _ in range(2)]
#
# x_max = max(num_list[0])
# y_min = min(num_list[1])
#
# if x_max >= y_min:
#     print('War')
# elif x_max < X or y_min > Y:
#     print('War')
# else:
#     print('No War')