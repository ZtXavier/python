def sushu(x):
    for i in range(2,x):
        if x % i == 0:
            return 0
    return 1


n = m = 0
for j in range(3,101,2):
    if sushu(j) == 1:
        m = n
        n = j
    if n - m == 2:
        print("%d %d"%(n,m))
        n = m = 0