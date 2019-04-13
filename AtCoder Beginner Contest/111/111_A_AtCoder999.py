n = [x for x in str(input())]
add_stock = ''

for i in n:
    add = i
    if i == '1':
        add = '9'
    elif i == '9':
        add = '1'
    add_stock += add

print(add_stock)
