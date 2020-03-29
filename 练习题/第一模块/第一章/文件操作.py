count=0
while count<3:
    user_name = input("请输入用户名称：")
    user_password = input("请输入密码：")
    massage=["seven:123","alex:456","angel:789"]
    user_massage=[user_name,user_password]
    sure=":".join(user_massage)
    if sure in massage:
        print("登录成功！")
        break

    else :
         print("用户名或者密码错误！")
         f=open(file=r'C:\Users\夏天\Desktop\用户状态.txt',mode='w',encoding='utf-8')
         f.write('用户名和密码输入超过三次，账户已被锁定，请找回账号和密码！')
         f.close()
         count += 1