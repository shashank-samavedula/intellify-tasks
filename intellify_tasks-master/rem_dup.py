def rem_dup(l):
    res = []
    for i in l:
        if i not in res:
            res.append(i)
    print(res)

l = [1,2,3,4,5,1,3,5]
rem_dup(l)
