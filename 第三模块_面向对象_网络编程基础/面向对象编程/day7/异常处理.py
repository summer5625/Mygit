# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 15:12
# @Author  : XiaTian
# @File    : 异常处理.py

# 猜年龄
# AGE = 18
# age = input('>>:').strip()
# if age.isdigit():   # 输入必须是数字
#     age = int(age)
#     if age > AGE:
#         print('猜大了！')
#     elif age < AGE:
#         print('猜小了')
#     elif age == AGE:
#         print('猜对了')
# else:
#     print('年龄必须是数字')


# try....excpet方式出异常
# try:
#     f=open('a.txt')
#     g=(line.strip() for line in f)
#     print(next(g))
#     print(next(g))
#     print(next(g))
#     print(next(g))
#     print(next(g))
#
# except StopIteration:
#     print('出错了')
# finally:
#     f.close()   # 不管有无异常都可以在文件打开后将其关闭
#
# print('===>1')
# print('===>2')
# print('===>3')

# 异常类只能用来处理指定的异常情况，如果非指定异常则无法处理
# 多分支
# try:
#     print('==>1')
#     # name
#     print('==>2')
#     a = [1,2,3]
#     # a[20]
#     print('==>3')
#     b = {}
#     # b['name']
# except Exception  as e:
#     print('错误信息：',e)
# except Exception as e:
#     print('错误信息：', e)
# except Exception as e:
#     print('错误信息：', e)
# else:
#     print('被检测代码块没有异常出现')    # 被检测代码块没有异常出现时才会触发
#
# finally:
#     print('不管被监测的代码块有无异常都会执行')


# class People:
#     def __init__(self, name, age):
#         if not isinstance(name,str):
#             raise TypeError('名字必须是字符串')
#         if not isinstance(age,int):
#             raise TypeError('年龄必须是数字')
#         self.name = name
#         self.age = age
# p = People(777,18)


# 断言：assert
info = {}
info['name'] = '夏天'
# info['age'] = 18

assert ('name' in info) and ('age' in info)


# class MyException(BaseException):  #  继承异常类
#     def __init__(self,msg):
#         super(MyException,self).__init__()
#         self.msg = msg
#
#     def __str__(self):
#         return '>>%s'%self.msg
#
# raise MyException('定义异常类型')  # raise会打印实例化的对象，要想显示异常值要定义一个__str__方法