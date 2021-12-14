n = int(input())
dict1 = {}
list1 = []
for step in range(n):
    st = input()
    a = ''
    for i in st:
        # 这里用isalpha函数来判断每行字符串是否是字母，若是小写字母，返回2,若是大写字母，返回1,若不是字母，返回0.
        if i.isalpha():                                  #因为这里需要单独判断每个字符是否为字母，然后依次预存到ae这个字符串变量中
            a += i.lower()
        elif a != '':
            if a in list1:
                dict1[a] += 1
                a = ''                                   #这里需要重新将a置为空
            else:
                list1.append(a)
                dict1[a] = 1
                a = ''
    if a != '':                             #这里是防止读到最后e一个字母后该循环跳出，没有处理a保存的字符串
         if a in list1:
                dict1[a] += 1
                a = ''                                   #这里需要重新将a置为空
         else:
             list1.append(a)
             dict1[a] = 1
             a = ''
list1.sort()
for i in list1:
    print(i,dict1[i])
            
    