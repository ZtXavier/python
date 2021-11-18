import sys
def f(arr,x,y):
    for i in range(len(arr)):
        if arr[i][y] < arr[x][y]:
            return False
    for i in range(len(arr[0])):
        if arr[x][i] > arr[x][y]:
            return False
    return True

def f1(t):
    res = []
    n,m = t[0][0],t[0][1]
    for x in range(n):
        for y in range(m):
            if f(t[1],x,y):
                res.append([t[1][x][y],x,y])
    return res

lines = sys.stdin.readlines()
data = []
i = 0
while i < len(lines):
    n,m = eval(lines[i].replace(' ',','))
    data.append(((n,m),tuple(map(lambda line:eval(line.replace(' ',',')),lines[i+1:i+n+1]))))
    i += n+1
for i in data:
    res = f1(i)
    if len(res) == 0:
        print("Not")
    for j in res:
        print(*j)