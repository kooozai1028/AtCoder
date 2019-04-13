s = int(input())

list = []

while s not in list:
    list.append(s)
    if s % 2 == 0:
        s //=  2
    else:
        s = 3*s + 1

print(len(list)+1)
