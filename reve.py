a = list(eval(input()))
rl = a[::-1]
ls = []
for i in range(len(a)):
    if rl[i] in ls:
        pass
    else:
        ls.append(rl[i])
print(ls[::-1])