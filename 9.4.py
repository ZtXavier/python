st = input()
b = []
b.append(st)
while(st != 'q'):
    st = input()
    b.append(st)
b.pop()

c = {}
for i in b:
    if i in c:
        c[i] += 1
    else:
        c[i] = 1
res = sorted(c.items(),key = lambda x : x[1],reverse= True)
n,m = res[0]
print("{} {}".format(n,m))


# b=[]
# b.append(a)
# while(a !="q"):
#     a=input()
#     b.append(a)
# b.pop()

# c={}
# for i in b:
#     if i in c:
#         c[i]=c[i]+1
#     else:
#         c[i]=1

# d=list(c.items())
# d.sort(key=lambda x:x[1],reverse=True)
# m,n=d[0]
# print("{} {}".format(m,n))