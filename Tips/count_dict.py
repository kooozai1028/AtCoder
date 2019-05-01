S = input()

def cnt_element(X):
    dict = {}
    for x in X:
        if x not in dict:
            dict[x] = 1
        else:
            dict[x] += 1
    return sorted([x for x in dict.items()],reverse=True,key=lambda x:x[1])

print(cnt_element(S))
