n = input()
ls = n.split()
dname = ls[0]
dscore = int(ls[1])
ms = dscore
md = dname
mis = dscore
mid = dname
sm = 0
k = 0

while n != "":
    ls = n.split()
    dname = ls[0] #这里不能将空字符串赋值给一个变量，会造成数组访问越界
    dscore = int(ls[1])
    if(dscore > ms):    
        ms = dscore
        md = dname
    elif(dscore < mis):    
        mis = dscore
        mid = dname
    k = k + 1
    sm += dscore
    n = input()
print("最高分课程是%s%d, 最低分课程是%s%d, 平均分是%.2f"%(md,ms,mid,mis,sm/k))