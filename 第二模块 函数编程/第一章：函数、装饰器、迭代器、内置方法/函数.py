# def message(name,age,course,country='CN'):     #默认参数country要放在后面
#
#     print(name,age,country,course)
# print('-----学生注册信息-----')
# message('何芳华',23,'python')
# message('夏云翔',25,'love')
# message('余承接',26,'c++','JB')               #当需要修改默认参数时，将修改的参数放在后面
# message('王战 ',23,'Java')


# def message(*names,age,course,country='CN'):   #在names前面加上*后使后面获得的名字是以元组形式打包
#     for i in names:
#         print(i,age,course,country)
# #方式一
# message('何芳华','夏云翔','余承接','王战 ',age=23,course='python')
#输出：
# 何芳华 23 python CN
# 夏云翔 23 python CN
# 余承接 23 python CN
# 王战  23 python CN
#方式二
# message(['何芳华','夏云翔','余承接','王战 '],age=23,course='python')  #如果不在列表前面加*，就会出现下面结果
#输出
#['何芳华', '夏云翔', '余承接', '王战 '] 23 python CN

#message(*['何芳华','夏云翔','余承接','王战 '],age=23,course='python')  #加了*则会出现方式一的结果


# def fu(name,*args,**kwargs):
#     print(name,args,kwargs)
# fu('何',22,'ali','50w')
#
# #输出
# # 何 (22, 'ali', '50w') {}
# fu('何',22,'ali','50w',course='python',bf='夏')
#
# #输出
# # 何 (22, 'ali', '50w') {'course': 'python', 'bf': '夏'}
#
# #问题用法
# a={'course': 'python', 'bf': '夏'}
# fu('何',22,'ali','50w',a)
# #输出
# # 何 (22, 'ali', '50w', {'course': 'python', 'bf': '夏'}) {}
#
# #正确用法
#
# fu('何',22,'ali','50w',**a)
# # 输出
# # 何 (22, 'ali', '50w') {'course': 'python', 'bf': '夏'}



#函数返回值

# def stu_register(name,age,course,country='CN'):
#     print('-----注册学生信息-----')
#     print('姓名：',name)
#     print('年龄：',age)
#     print('课程：',course)
#     print('国家：',country)
#     if age>22:
#         return {name:age}
#     else:
#         return {name:age}
#     # return
#
# registriation_status = stu_register('余承接',26,'如何学装逼')
# print(registriation_status)
# if registriation_status:
#     print('注册成功')
# else:
#     print('too old to be a student.')


#修改列表
# name=('何芳华','love','夏')
#
# def lv():
#
#     name = ('何芳华','love')
#     print(name,id(name) )
#
# lv()
# print(name,id(name))




#嵌套函数
# age=25
# def f1():
#     age=18
#     print(age)
#     def f2():
#         age=26
#         print(age)
#     f2()
# f1()
#
# age=25
# def f1():
#     # age=18
#     #print(age)
#     def f2():
#         # age=26
#         print(age)
#
#     age = 18
#     f2()
#
# f1()


# age=18
# def f1():
#     age=56
#     print(age)
#     def f2():
#         age=27
#         print(age)
#
#     return f2
# val=f1()
# val()     #val（）执行的是f2的函数
# print(val)


a = '23'
b= eval(a)
print(type(b))
