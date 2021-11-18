def deal_(n):
    lis_ = [0] * n
    for i in range(n):
        lis_[i] = input().split()
    sum = []
    sum0 = 1
    for i in range(n):
        for j in range(3):
            lis_[i][j] = int(lis_[i][j])
            sum0  = sum0 * lis_[i][j]
        sum.append(sum0)
        sum0 = 1
    i = sum.index(max(sum))
    name2 = lis_[i][3]
    i = sum.index(min(sum))
    name1 = lis_[i][3]
    print("%s took clay from %s."%(name2,name1))
    
    n = int(input())
    if n != -1:
        deal_(n)
    else:
        pass
    
n = int(input())
if n != -1:
    deal_(n)
else:
    pass