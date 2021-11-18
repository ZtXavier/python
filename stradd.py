#任意多行字符串求和
la=[]
while True:
    try:
        x=input()
        if x=='':break
        la.append(x)
    except:
        break
for y in la:
    z=y
    z=z.replace(';',' ')
    z=z.replace(',',' ')
    z=str.split(z)
    z=map(int,z)
    print("%s:%d"%(y,sum(z)))