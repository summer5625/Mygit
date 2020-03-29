count=0
#基础需求
# while count<3:
#     user_name = input("请输入用户名称：")
#     user_password = input("请输入密码：")
#     if user_name=="seven"  and user_password=="123":
#         print("登录成功！")
#         break
#     count +=1
#     if count==3:
#          print("用户名或者密码错误！")

#升级需求一
while count<3:
    user_name = input("请输入用户名称：")
    user_password = input("请输入密码：")
    massage=["seven:123","alex:456","angel:789"]
    user_massage=[user_name,user_password]
    sure=":".join(user_massage)
    if sure in massage:
        print("登录成功！")
        break
    else:
        print("用户名或者密码错误！")

        count +=1
    if count==3:
         print("用户名或者密码错误！")
         