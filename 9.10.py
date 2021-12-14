dict1 = {'admin':'123456','administrator':'12345678','root':'password'}
# 将用户的密码和账户分别存在一个列表中
users = list(dict1.keys())
passwds = list(dict1.values())

j = 0
while(j < 3):
    inuser = input()
    inpasswds = input()
    if inuser in users:
        pos = users.index(inuser)              # 取下标来进行判断，也可以直接操作字典
        if inpasswds == passwds[pos]:
            print("登录成功")
            break
        else:
            j = j + 1
            print("登陆失败")
    else:
        print("登陆失败")
        j = j + 1
    