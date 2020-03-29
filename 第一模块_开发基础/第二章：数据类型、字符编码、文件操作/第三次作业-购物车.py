#! -*- coding:utf-8 -*-
user_message={'he':'123','fang':'456','hua':'789'}
goods=[{'name':'电脑','price':1999},{'name':'鼠标','price':10},{'name':'游艇','price':20},
       {'name':'美女','price':998},{'name':'消费记录','price':''}]
run_flag=True
count=0
miss_user=[]  #记录输错的账号
shopping_cart=[]  #记录购已购买的商品
f = open(file=r'C:\Users\夏天\Desktop\锁定账号.txt',mode='r',encoding='utf-8')   #读取用户状态，判断用户是不是被锁定
lock_user = f.readlines()
f.close()
number=0

#用户登录程序
while count<3:
    user_name = input('请输入用户名：')
    user_password = input('请输入密码：')
    if user_name not in lock_user:
        if user_name in user_message:
            if user_password==user_message[user_name]:
                print("登录成功")
                f = open(file=r'C:\Users\夏天\Desktop\登录用户.txt', mode='w', encoding='utf-8')  #将登录成功用户，状态存储起来
                f.write(user_name)
                f.close()
                break
            else:
                 print('用户名或密码错误，请重新输入！')
                 miss_user.append( user_name)
                 print(len(miss_user))
            if len(miss_user)==3:
                     print('用户名或密码输错次数太多，账号已被锁定！')
                     f = open(file=r'C:\Users\夏天\Desktop\锁定账号.txt',mode='w',encoding='utf-8')  #将密码输错三次的账号锁定
                     f.write('%s' % miss_user[0])
                     f.close()
        else:
            print('该用户未注册！')
            count+=1
    else:
        print('账号已被锁定，请询问管理员解锁！')

#购买商品程序

f = open(file=r'C:\Users\夏天\Desktop\登录用户.txt',mode='r',encoding='utf-8')   #读取用户状态，判断用户是不是登录过
land_user = f.readlines()
f.close()
if user_name in land_user:
    f = open(file=r'C:\Users\夏天\Desktop\消费记录.txt', mode='r', encoding='utf-8')  # 读取用户消费记录
    merry_shopping = f.readlines()
    f.close()
    if len(merry_shopping)==0:
        money=int(input('请输入您的收入：'))
        while run_flag:
            print("-------商品列表-------")
            for i in goods:  # 打印商品列表
                print(number, i['name'], i['price'])
                number += 1
            choice = input("请输入要购买的商品编号：")
            if choice.isdigit():
                choice = int(choice)
                if len(goods)>choice and choice>= 0:
                    pay_money = goods[choice]['price']
                    if money >= pay_money:  # 判断余额是否充足
                        shopping_cart.append(goods[choice])
                        print("\033[1;31;47m")
                        print(goods[choice]['name'], goods[choice]['price'], "已购买！")
                        print('\033[0m')
                        money = money - pay_money  # 计算购买商品后的余额
                        print("\033[0;31;47m")
                        print('当前余额：',money)
                        print('\033[0m')
                        number = 0
                    else:
                        print('哈哈哈，你个屌丝买不起吧！')
                else:
                    print("无此商品，请重新选择商品！")
                    number = 0
            elif choice == 'q':
                if len(shopping_cart) > 0:
                    print("------以下商品已购买------")
                    for i in shopping_cart:
                        print(i['name'],i['price']  )
                    print("\033[1;31;43m")
                    print('------您的余额为：%s------'%(money))
                    print('\033[0m')
                    f = open(file=r'C:\Users\夏天\Desktop\消费记录.txt', mode='w', encoding='utf-8')  # 记录退出程序时的消费情况
                    f.write('%s\n' % shopping_cart)
                    f.close()
                    f = open(file=r'C:\Users\夏天\Desktop\余额记录.txt', mode='w', encoding='utf-8')  # 记录退出程序时的消费情况
                    f.write('%s\n' % money)
                    f.close()
                run_flag = False
    else:
         f = open(file=r'C:\Users\夏天\Desktop\余额记录.txt', mode='r', encoding='utf-8')  # 读取用户消费记录
         money=f.readlines()
         f.close()
         money_left=int(money[0])
         print("\033[0;31;47m")
         print('您的余额为：',money_left)
         print('\033[0m')
         while run_flag:
            print("-------商品列表-------")
            for i in goods:  # 打印商品列表
                print(number, i['name'], i['price'])
                number += 1
            choice = input("请输入要购买的商品编号：")
            if choice.isdigit():
                choice = int(choice)
                if len(goods) > choice and choice >= 0:
                    pay_money = goods[choice]['price']
                    if int(money[0])>= pay_money:  # 判断余额是否充足
                        shopping_cart.append(goods[choice])
                        print("\033[1;31;47m")
                        print(goods[choice]['name'], goods[choice]['price'], "已购买！")
                        print('\033[0m')
                        money_left =  money_left - pay_money  # 计算购买商品后的余额
                        print("\033[0;31;47m")
                        print('当前余额：', money_left)
                        print('\033[0m')
                        number = 0
                    else:
                        print('哈哈哈，你个屌丝买不起吧！')
                else:
                    print("无此商品，请重新选择商品！")
                    number = 0
            elif choice == 'q':
                if len(shopping_cart) > 0:
                    print("------以下商品已购买------")
                    for i in shopping_cart:
                        print(i['name'], i['price'])
                    print("\033[1;31;43m")
                    print('------您的余额为：%s------' % (money_left))
                    print('\033[0m')
                    f = open(file=r'C:\Users\夏天\Desktop\消费记录.txt', mode='w', encoding='utf-8')  # 记录退出程序时的消费情况
                    f.write('%s\n' % shopping_cart)
                    f.close()
                run_flag = False