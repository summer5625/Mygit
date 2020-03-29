count=0
while count<3:
    user_name = input("请输入用户名称：")
    user_password = input("请输入密码：")
    if user_name=="seven"  and user_password=="123":
        print("登录成功！")
    if user_name=="alex"  and user_password=="123":
        print("登录成功！")
        break
    count +=1
    if count==3:
         print("用户名或者密码错误！")