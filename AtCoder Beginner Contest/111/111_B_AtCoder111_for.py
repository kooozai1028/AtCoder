N = 112
repdigit = [str(x)*3 for x in range(1,10)]

for i in range(len(repdigit)):
    try:
        if N <= int(repdigit[i]):
            print(repdigit[i])
            brea_fk
    except:
        pass
