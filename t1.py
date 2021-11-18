ls = []
ls = [i for i in input().split()]
l = int(ls[0])
m = 0
for i in range(1,l):
    ls[i],ls[l-i+1] = ls[l-i+1],ls[i]
    m += 1
    if(m == (l-1)//2):
        break
for i in range(1,l+1):
    if(i != (l)):
        print(ls[i],end =' ')
    else:
        print(ls[i],end = "\n")