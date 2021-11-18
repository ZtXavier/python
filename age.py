def age(x,i):
    if i == 1:
        return 10
    else:
        return 2 + age(x+2,i-1)

m,n = map(int,input().split())    #输入多个数字的技巧
res = age(m,n)
print("%d"%res)
