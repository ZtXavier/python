n = int(input())
strs = []
for i in range(n):
    strs.append(input())
nums = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
data = {0:1,1:0,2:'X',3:9,4:8,5:7,6:6,7:5,8:4,9:3,10:2}

t = True

for ch in strs:
    s = True
    sum = 0
    for i in range(17):
        print("%d\n"%i)
        if '0' <= ch[i] <= '9':
            sum += int(ch[i]) *nums[i]
    if s:
        Z = sum % 11
        if str(data[Z]) != ch[17]:
            t = False
            print(ch)
    else:
        t = False
        print(ch)
if t:
    print("All passed")