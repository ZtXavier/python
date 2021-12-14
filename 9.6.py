m,n = map(int,input().split())
while m != 0 and n != 0:
    dict1= {}
    for i in range(m):
        k,v = map(str,input().split(':'))                                #这里根据题目意思来将':'作为分隔符
        dict1[k] = v
    ending = 1
    for i in range(n):
        word = input()
        if ending == 1:
            print(dict1.get(word,'Not found!'),end=' ')
            ending = 0
        else:
            print()                                                               #保证其输出的格式
            print(dict1.get(word,'Not found!'),end=' ')
    n,m=map(int,input().split())