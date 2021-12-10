num = int(input())
for _ in range(num):
    res = input()
    try:
        result = eval(res)
    except NameError:
        print("NameError")
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except SyntaxError:
        print("SyntaxError")
    else:
        print("%.2f"%result)
