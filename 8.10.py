while True:
    try:
        n = int(input())
        m = n + 2
        l, li, uplist = [0], [], []
        # 输入给定矩阵
        for j in range(1, n + 1):
            li.append(input().split())
        # 构造新矩阵
        for i in range(1, m + 1):
            if i == 1:
                uplist.append(l * m)
            elif i == m:
                uplist.append(l * m)
            else:
                x = i - 2
                uplist.append(l + li[x] + l)
 
        # 矩阵字符型化为整数
        for i in range(1, n + 1):
            uplist[i] = list(map(int, uplist[i]))
 
        cnt = 0
        # 外层两个循环遍历矩阵每一个元素
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                f1 = 1
                listx = [1, 0, -1]
                # 内层两个循环遍历一个元素正方形个元素
                for k in listx:
                    for l in listx:
                        # 跳过自身对比
                        if k == 0 and l == 0:
                            continue
                        # 发现小于等于自己的，不满足为局部峰值
                        if uplist[i][j] <= uplist[i + k][j + l]:
                            f1 = 0
                # 矩阵一个数周围都比他小f=1
                if f1 == 1:
                    print(uplist[i][j], end=' ')
                    cnt = cnt + 1
        # 存在一个元素
        if cnt > 0:
            print()
        else:
            print("none")
    except:
        break