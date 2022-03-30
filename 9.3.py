T = eval(input())
for z in range(T):
    n,nm=input().split()
    n = eval(n)
    canaward = int(n*0.6+0.5)   #加0.5目的为了进位
    lstS=[]
    lstM=[]
    lstG=[]
    lst=[]
    for i in range(n):
        s,m,g = input().split()
        m,g=int(m),int(g)                        # 排序是将每个队伍的得分和解题数分别存到一个序列中，然后定位取值
        lstS.append(s)
        lstM.append(m)
        lstG.append(g)
        nameindex = lstS.index(nm)
        grade = lstG[nameindex]
        lstG.sort(reverse=True)
        sortedindex = lstG.index(grade)
        if sortedindex <= canaward-1:
            print("YES")
        else:
            print("NO")
        
    