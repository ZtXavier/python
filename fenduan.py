n = input()
n = float(n)
if n == 0:
    ret = 0
else:
    ret = 1/n
print("f(%.1f) = "%n + "%.1f"%ret)