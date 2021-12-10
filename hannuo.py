def hanuo(n,x,y,z):
    if n == 1:
        print(x,"-->",z)
    else:
        hanuo(n-1,x,z,y)
        print(x,"-->",z)
        hanuo(n-1,y,x,z)
n = eval(input("请输入层数"))
hanuo(n,'x','y','z') 