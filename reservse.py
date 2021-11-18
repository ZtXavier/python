n = int(input())
while n > 0:
    ls = []
    ls = [i for i in input().split()]
    a = int(ls[1])
    b = int(ls[2])
    m = 0
    for i in range(a+2,b+3):
        ls[i],ls[b-i+a+4] = ls[b-i+a+4],ls[i]     #py的特殊置换方式
        m += 1
        if(m == (b-a+1)//2):
            break
    n -= 1
    for i in range(len(ls)-3):
        if(i != (len(ls) - 4)):
            print(ls[i+3],end=" ")
        else:
            print(ls[i+3],end="\n")



#             n = 0
# while True:
#     try:
#         n += 1
#         ls = []
#         ls = [i for i in input().split()]
#         l = int(ls[0])
#         m = 0
#         for i in range(1,l):
#             ls[i],ls[l-i+1] = ls[l-i+1],ls[i]
#             m += 1
#             if(m == (l-1)//2):
#                 break
#         for i in range(1,l+1):
#             if(i != (l)):
#                 print(ls[i],end =' ')
#             else:
#                 if(n == 2):
#                     print(ls[i],end = '\n')
#                 else:
#                     print(ls[i],end = '\n\n')
#     except:
#         break