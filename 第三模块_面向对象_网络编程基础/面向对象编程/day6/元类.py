# -*- coding: utf-8 -*-
# @Time    : 2019/3/9 22:09
# @Author  : XiaTian
# @File    : 元类.py


# exec(object,globals,locals)使用

'''
    exec有三个参数:
    object:字符串形式的命令，即一段字符串形式的代码
    globals：全局作用域，必须是字典形式的；如不指定，默认为globals
    locals：局部作用域，必须是字典；如不指定，默认locals
'''
# 可以把exec命令的执行当成是一个函数的执行，会将执行期间产生的名字存放于局部名称空间中
# g = {'x':1,'y':2}
# l = {}
# exec('''
# global x,m
# x = 100
# m = 10
# z = 50
#     ''',g,l)
#
#
# print(g['m'])
# print(l)


# 元类
# 一切皆对象
class Foo:
    pass

# f = Foo()
# print(type(Foo))
# print(type(f))
#
# print(type(type))

# 产生类的两种方式
# 方式一：用class关键字
# 手动模拟class创建类的过程）：将创建类的步骤拆分开，手动去创建，即type模式

# 定义类的三要素
# 1、类名
class_name = 'Chinese'

# 2、父类
class_bases = (object,)               # 不加逗号，会报错

# 3、名称空间
class_body = '''
country='China'
def __init__(self,name,age):          # 类体代码，字符串形式
    self.name=name
    self.age=age
def talk(self):
    print('%s is talking' %self.name)
'''

class_dict = {}                       # 分配类的名称空间
exec(class_body,globals(),class_dict) # 调用exec()创建类
print(class_dict)

Chinese = type(class_name,class_bases,class_dict)  # 创建元类为type的类
print(Chinese)

p = Chinese('夏天',18)
print(p)
print(p,p.name,p.age)
p.talk()
print(type(Foo))
print(type(Chinese))
