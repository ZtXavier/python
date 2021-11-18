# st = input()
# a,b = input().split()
# #下面的语句将在st字符串中遍历，如果遇到与a或b相同的则输入到lst1中
# lst1 = [(i,st[i]) for i in range(len(st)) if st[i] == a or st[i] == b]
# lst2 = lst1[::-1]
# for i in range(len(lst2)):
#     print(lst2[i][0],lst2[i][1])


s=input()
#enumerate内置函数将输入的字符串变为具有索引的序列(可以进行序列号的默认值初始化)
lst=list(enumerate(s))
char1,char2=input().split()
l=[(i,s[i]) for i in range(len(s)) if lst[i][1]==char1 or lst[i][1]==char2]
l.reverse()
for v in l:
    print(v[0],v[1])