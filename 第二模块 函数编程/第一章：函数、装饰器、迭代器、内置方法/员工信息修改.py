import os

#从文件中读员工信息

def read_msg():
    msg = []
    f = open('员工信息表.txt','r',encoding = 'utf-8')
    for i in f:
        i.strip()
        i=i[:-1]                                        #去掉换行符
        msg_i = i.split(',')                            #将读到的字符串转换成列表
        msg_i[5] = msg_i[5].split('-')
        msg_i[2] = int( msg_i[2])
        msg_i[0] = int( msg_i[0])
        msg.append(msg_i)
    f.close()
    return msg

#将修改的信息存到文件中

def save_file(msg):
    f = open('员工信息表.txt', mode='w', encoding='utf-8')
    for i in msg:
        a = '{0}-{1}-{2}'
        b = i
        i[5] = a.format(b[5][0],b[5][1],b[5][2])                       #将员工入职时间转换成字符串
        a_staff = '{0},{1},{2},{3},{4},{5}\n'
        a_staff = a_staff.format(i[0], i[1], i[2], i[3], i[4], i[5])   #将员工信息转换成字符串
        f.write(a_staff)
    f.close

#员工信息查询

def find_msg_by_depet():
    count = 0
    msg = read_msg()
    m_msg = read_msg()
    w_msg = []
    for j in m_msg:                                       #将员工信息中不作为查找关键字的信息剔除
        j.append(j[5][0])
        j.remove(j[5])
        j.remove(j[0])
        w_msg.append(j)
    flag = True
    while flag:
        key_msg = input('请输入要查询的关键字：').strip()
        if key_msg.isdigit():
            key_msg = int(key_msg)
            if key_msg <100:                               #判断输入的是不是年龄
                for i in w_msg:
                    if i[1] > key_msg:
                        print(i[0],i[1])
                        count += 1
                print('共查找到%s条结果' % (count))
                count = 0
            elif key_msg<10000:                            #按照年份查找
                for k in msg:
                    if key_msg == int(k[5][0]):
                        print(k)
                        count += 1
                print('共查找到%s条结果' % (count))
                count = 0
            else:                                           #按照电话查找
                for k in msg:
                    if key_msg == int(k[3]):
                        print(k)
                        count += 1
                print('共查找到%s条结果' % (count))
                count = 0

        elif key_msg == 'q':                               #退出查找功能，返回主菜单
            flag = False

        else:                                               #按照员工姓名和部门查找
            for n in msg:
                if key_msg in n:
                    print(n)
                    count += 1
            print('共查找到%s条结果'%(count))
            count = 0



#新员工添加

def add_new_staff():
    flag = True
    count = 0
    while flag:
        msg = read_msg()
        id = len(msg)
        name = input('员工姓名：').strip()
        if name != 'q':
            flag1 = True
            age = input('员工年龄：').strip()
            if age.isdigit():                        #判断输入的年龄是不是符合常理的，是则转换成数字格式
                age = int(age)
            else:
                print('请输入正确年龄！')
                continue                             #年龄格式不对结束本次循环
            while flag1:
                for i in msg:                        #将员工的电话号码提取出来
                    numbers = []
                    numbers.append(i[3])
                number = input('电话：').strip()
                while True:
                    if number not in numbers:        #判断输入的电话号码在不在员工信息里面
                        r_number = number
                        flag1 = False
                        break
                    else:                            #输入号码重复，则重新输入
                        print('电话号码与他人重复，请重新输入！')
                        break
            depet = input('部门：').strip()
            enroll_date = input('入职时间(格式为：xxxx-xx-xx):')
            a_staff = '{0},{1},{2},{3},{4},{5}\n'
            a_staff = a_staff.format(id+1,name,age,r_number,depet,enroll_date)

            f=open('员工信息表.txt','a',encoding = 'utf-8')
            f.write(a_staff)
            f.close()
            count += 1
        else:                                          #退出添加新员工功能返回主菜单
            flag = False

    print('已添加%s信息'%(count))


#批量员工部门信息修改

def change_msg1():
    count = 0
    flag = True
    while flag:
        key_dept = input('请输入要修改的部门：')
        if key_dept != 'q':
            msg = read_msg()
            depts = []
            for i in msg:                                 #将员工的部门提取出来，放到一个列表中
                depts.append(i[4])
            if key_dept in depts:                         #判断输入的部门是不是公司的部门，如果不是重新输入
                c_dept = input('请输入修改后的部门：')
                for k in msg:
                    if key_dept in k:                     #修改符合条件的员工部门信息
                        k[4] = c_dept
                        count += 1                        #记录修改了多少条信息
                save_file(msg)
            else:
                print('请输入正确的部门')
                continue
        else:
            flag = False
        print('本次操作修改了%s条信息' % (count))

#个人信息修改

def change_msg2():
    count = 0
    flag = True
    while flag:
        l_name = input('请输入要修改员工的姓名:').strip()
        if l_name != 'q':
            msg = read_msg()
            names = []
            for i in msg:                                              #将员工的姓名提取出来
                names.append(i[1])
            if l_name in names:                                        #判断是不是输入员工在不在公司
                for i in msg:
                    if l_name in i:
                        old_msg = i
                        for index, k in enumerate(old_msg):            #打印要修改员工的信息
                            if index > 0:
                                print("%s.  %s" % (index, k))
                        choice = input("选择要修改的信息编号:").strip()  #选择要修改员工的那条信息
                        if choice.isdigit():
                            choice = int(choice)
                            if choice > 0 and choice < len(old_msg):   #判断输入的编号是不是超出了
                                K_msg = old_msg[choice]
                                print('原信息：', K_msg)
                                cd_msg = input('输入新信息：').strip()
                                if cd_msg:                            #判断修改的信息是不是空的，是空的就重新输入
                                    old_msg[choice] = cd_msg
                                    count += 1
                                    save_file(msg)
                                else:
                                    print("不能为空。。。")
            else:
                print('查无此人，请重新输入')
                break
            print('本次修改了%s条员工信息'%(count))
        else:
            flag = False

#删除员工信息

def del_msg():
    flag = True
    count = 0
    while flag:
        msg = read_msg()
        l_id = []
        for index, k in enumerate(msg):                             #打印员工信息
            print(index+1,k[1],k[2],k[3],k[4])
        id = input("输入要删除员工的ID：").strip()
        if id != 'q':                                               #判断是不是要返回主菜单
            if id.isdigit():
                id = int(id)
                for i in msg:                                       #将员工的ID提取出来
                    l_id.append(i[0])
                if id in l_id:                                      #将符合条件的员工信息删除
                    del msg[id-1]
                    save_file(msg)
                    count += 1
                else:
                    print('请输入正确的员工ID')                      #输入的ID超出了公司员工数量返回重新输入

        else:
            print('删除了%s条员工信息' % (count))
            flag = False

#功能菜单

def function():
    print('-----员工信息管理系统-----')
    print('1、员工信息查询')
    print('2、批量员工部门信息修改')
    print('3、个人信息修改')
    print('4、员工信息删除')
    print('5、增加新员工信息')
    print('返回主菜单请按b')
    print('退出请按q')
f = True
while f:
    function()
    chioce = input('请输入操作序号：').strip()
    if chioce.isdigit():              #判断是不是数字
        chioce = int(chioce)
        if chioce ==1:
            find_msg_by_depet()
        elif chioce == 2:
            change_msg1()
        elif chioce == 3:
            change_msg2()
        elif chioce == 4:
            del_msg()
        elif chioce == 5:
            add_new_staff()
        else:
            print('请输入正确的序号')   #超出功能数量返回主菜单
    elif chioce == 'b':               #返回主菜单
        function()
    elif chioce == 'q':
        f = False



