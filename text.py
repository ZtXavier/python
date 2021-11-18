# ls = []
# ls = [int(i) for i in input().split()]
# ls.reverse()
# print(ls)

b_list = input()
a_list = []
for i in b_list.split(','):
    a_list.append(i)
print(a_list)
a_list.reverse()
print(a_list)
