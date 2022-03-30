ret = []
s = input().split()
s = list(s)
if len(s) == 0:
    print(ret)
h = input().split()
h = list(h)

ret1 = []
for i in s:
    for j in h:
        if i.lower() == j.lower():
            ret1.append(i)
for i in s:
    if i not in ret1:
        ret.append(i)
            
k = len(ret)
m = 0
for i in ret:
    m = m+1
    if m == k:
        print(i,end="")
    else:
        print(i,end=" ")