#登录程序

# f = open('个人信息.txt','w+',encoding='utf-8')
# f.write('夏天,abc123,27,中国.河南,13469771735,python\n')
# f.write('何芳华,abc123,22,中国.东莞,17634407602,love\n')
# f.write('朱正阳,abc123,21,中国.河南江,18722046768,C++\n')
# f.write('王战,abc123,25,中国.湖北,18827558956,python\n')
# f.close()



#用户名确认，如果输入用户名在文件中，则返回用户名所在行的信息
def sure_name(x):
    f = open('个人信息.txt','r',encoding='utf-8')
    for i in f:
        i.strip()
        msg = i.split(',')
        if x == msg[0]:
            return msg
    f.close()

#密码确认，如果密码正确则进入功能选择菜单
def sure_pwd(y):
        msg = sure_name(user_name)
        if msg != None:
            if y == msg[1]:
                print('----登录成功！----')
                return True
            else:
                print('用户名或者密码错误！')
        else:
            print('用户未注册！')

def show_msg(number):
    if number == 1:
        p_msg = sure_name(user_name)
        print('-----个人信息-----')
        print('姓名：',p_msg[0])
        print('年龄：',p_msg[2])
        print('籍贯：',p_msg[3])
        print('电话：',p_msg[4])
        print('课程：',p_msg[5])


def change_pwd(number):
    if number == 3:
        c_msg = sure_name(user_name)
        old_pwd = input('请输入原密码：').strip()
        new_pwd = input('请输入新密码：').strip()
        if old_pwd == c_msg[1]:
            c_msg[1] = new_pwd
            new_msg = ','.join(c_msg)
        f_old = open('个人信息.txt', mode='r', encoding='utf-8')
        f_new = open('个人信息.txt.new', mode='w', encoding='utf-8')
        for lin in f_old:
            if user_name in lin:
                lin = lin.replace(lin,new_msg)
        f_new.write(lin)
        f_old.close()
        f_new.close()
        os.remove('个人信息.txt')
        os.renames('个人信息.txt.new','个人信息.txt')

def change_msg(number):
    if number == 2:
        old_msg = sure_name(user_name)
        for index, k in enumerate(old_msg):
            if index > 1:
                print("%s.  %s" % (index, k))
        choice = input("选择要修改的信息编号:").strip()
        if choice.isdigit():
            choice = int(choice)
            if choice > 0 and choice < len(old_msg):
                c_msg = old_msg[choice]
                print('原信息：',c_msg)
                cd_msg = input('输入新信息：').strip()
                if c_msg:
                    old_msg[choice] = cd_msg
                    new_msg = ','.join(old_msg)
                else:
                    print("不能为空。。。")
        elif choice == 'q':
            exit("拜拜！")


        f_old = open('个人信息.txt', mode='r', encoding='utf-8')
        f_new = open('个人信息.txt.new', mode='w', encoding='utf-8')
        for lin in f_old:
            if user_name in lin:
                lin = lin.replace(lin,new_msg)
            f_new.write(lin)
        f_old.close()
        f_new.close()
        os.remove('个人信息.txt')
        os.renames('个人信息.txt.new','个人信息.txt')

import os
count=0
while count<3:
    user_name = input('请输入用户名：').strip()
    user_pwd = input('请输入密码：').strip()
    flog = sure_pwd(user_pwd)
    if flog:
        print('-----请选择要执行操作的序号-----')
        print('1、打印个人信息')
        print('2、修改个人信息')
        print('3、修改密码')
        number = input('请输入要操作的序号：').strip()
        if number.isdigit():
            number = int(number)
        if number == 1:
            show_msg(number)
        elif number == 2:
            change_msg(number)
        elif number ==3:
            change_pwd(number)

        break
    else:
        count+=1
# def save_file(x)
#
#         f_old = open('个人信息.txt', mode='r', encoding='utf-8')
#         f_new = open('个人信息.txt.new', mode='w', encoding='utf-8')
#         for lin in f_old:
#             if user_name in lin:
#                 lin = lin.replace(lin,new_msg)
#             f_new.write(lin)
#         f_old.close()
#         f_new.close()
#         os.remove('个人信息.txt')
#         os.renames('个人信息.txt.new','个人信息.txt')
#







