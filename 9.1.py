count = 0
ls = []
while True:
    s = input()
    if s == "!!!!!":
        break;
    a = s.split()
    for item in a:
        if item not in ls:
            count = count + 1
            ls.append(item)
ls.sort()
print(count)
if count <= 10:
    for i in range(count):
        print(ls[i])
else:
    for i in range(10):
        print(ls[i])    