def dg(x,n):
    if n == 0:
        return 1
    else:
        return n*dg(x,n-1)


n,x = map(int,input().split())
res = dg(n,x)
print("%d"%res)