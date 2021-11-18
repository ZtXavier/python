n = eval(input())
words=""
while n > 0:
    
    a=input()
    a=a.lower()
    for i in "!.,:*?":   #将不需要的字符用空格替换掉
        a=a.replace(i,' ')
    for i in "0123456789":
        a = a.replace(i,' ')
    words=words+" "+a
    n -= 1
words=words.split()
s={}
for i in words:
    if i in s:
        s[i]+=1
    else:
        s[i]=1
s=list(s.items())

s.sort(key=lambda x:x[0])
# s.sort(key=lambda x:x[1],reverse=True)
# print(len(s))
for i in range(len(s)):
    word,count=s[i]
    print("{} {}".format(word,count))