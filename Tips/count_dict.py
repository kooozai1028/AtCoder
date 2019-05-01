def cnt_element(x):
    dict = {}
    for i in x:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    return  sorted([x for x in dict.values()],reverse=True)
