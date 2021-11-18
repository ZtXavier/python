while True:
    try:
        flag = 1
        n,m = map(int,input().split())
        arr = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                arr[i][j] = eval(input().split())
        maxn = arr[0][0]
        for i in range(n):
            for j in range(m):
                if maxn < arr[n][m]:
                    maxn = arr[n][m]
                    k = i;
                    l = j;
            minn = arr[k][l]
            for h in range(n):
                if minn > arr[h][l]:
                    minn = arr[h][l]
            if maxn == minn:
                flag = 0
                print("%d %d %d"%(maxn,k,j))
        if flag == 1:
            print("Not")
        flag = 1
    except:
        break



# while True:
#     try:
#         st = input()
#         ln = [0]*256
#         for i in st:
#             ln[ord(i) - 48] += 1
#         for i in range(256):
#             if(ln[i] != 0):
#                 print("%c %d"%(chr(i+48),ln[i]))
#     except:
#         break