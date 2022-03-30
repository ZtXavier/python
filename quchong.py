a = list(eval(input()))
b = []
for i in a:
    if i not in b:
        b.append(i)
for i in b:
    if i == b[-1]:
        print(i)
    else:
        print(i,end=' ')
