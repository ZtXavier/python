n =int(input())
a = []

for i in range(n):
    a.append(list(map(int,input().split())))
min = []

# 找列上的最小值
for i in range(n):
    m = a[0][i]
    for j in range(n):
        if a[j][i] < m:
            m = a[j][i]
    min.append(m)
    
# 调用max函数来比较一个列表的最大值
f = False
for i in range(n):
     for j in range(n):
         if a[i][j] == max(a[i]) and a[i][j] == min[j]:
             print(i, j)
             t = True
if f == False:
    print("NONE")