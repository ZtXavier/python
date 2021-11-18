for i in range(2,1001):
    ls = []
    s = 0
    for j in range(1,i):
        if i%j == 0:
            ls.append(j)
            s += j
    if s == i:
        print("%d its factors are:"%i,ls)
