a = input()
a = int(a)
sum = 0
if a >= 0:
    if a <=50:
        sum += a*0.53
    elif a > 50:
        sum += 50*0.53+(a-50)*0.58;
    print("cost = %.2f"%sum)
else:
    print("Invalid Value!")
    