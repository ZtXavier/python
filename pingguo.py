n,x,y = eval(input())
if n != 0:
    if (y/x) > (y//x):
        num = y//x+1
        n -= num
    elif (y/x) > 0:
        if (y/x) >0 and y/x < 1:
            n -= n
        else:
            n -= y//x
else:
    n = 0
print(n)
        
    