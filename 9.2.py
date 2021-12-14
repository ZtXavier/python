dict1 = {}
sum1 = 0
while True:
    st = input()
    lis = list(st.lower().split())
    if len(lis) == 0:                              #判断两部分，一部分判断是否读入数据，另一部分判断当读入数据后的对子符的处理
        continue
    else:
        if "!!!!!" in lis:                           # 如果有五个感叹号出现则终止
            break
        for i in lis:
            for q in "!.*,:*?":                     #这里巧妙地运用循环来依次判断是否有需要删除的符号
                i = i.replace(q,'')
            if i.lower() in dict1:
                dict1[i.lower()] += 1   
            else:
                dict1[i.lower()] = 1
sum1 = len(dict1)
print(sum1)
sum1 = 0
for i in sorted(dict1.items(),key = lambda x : (-x[1],x[0])):                  # 这里的匿名函数作用是先进行值的降序排序，如果值相同则根据首字母字典序排序
    if sum1 == 10:
        break
    print("%s=%d"%(i[0],i[1]))
    sum1 += 1
    