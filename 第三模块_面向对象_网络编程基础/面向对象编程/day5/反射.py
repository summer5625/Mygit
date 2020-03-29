# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 21:49
# @Author  : XiaTian
# @File    : 反射.py


class Foo:
    pass


class Son(Foo):
    pass


f = Foo()


# 判断对象是不是类的对象
# print(isinstance(f,Foo))  # isinstance(f,Foo)需要两个参数，第一个是要判断的对象，第二个是对象属于的类。是返回True,不是返回False

# 判断两个类是不是派生类

# print(issubclass(Son,Foo)) # issubclass()需要传两个参数，第一个是要判断的对象，第二个是父类。是则返回True，不是返回False


# 反射：通过字符串来映射对象的属性，即通过字符串的输入来执行相应功能的代码 eval()

class People:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print('name:%s  age:%s' % (self.name, self.age))
        return 456

    @staticmethod
    def trys():
        return 'trys'


p = People('夏天', 25)

# 判断对象是否有相应的属性，hasattr(obj,str)有两个参数，obj是要判断的对象，str必须是字符串类型的变量，代表obj对象里面有无str的变量

# print(hasattr(p,'name')) # 实际上是在判断p.__dict__['name']字典里面有没有name的变量
# print(hasattr(p,'talk')) # 判断p里面有没有talk的函数属性
# print(p.__dict__)
# 获取属性的值
# getattr(obj,str,default) 有三个参数，最后一个参数可以不填，str中的参数必须是字符串
# n = getattr(p,'name')   # 实际上是获取p.name的值
# print(n)
b = getattr(p, 'name456', p.talk())  # 填了第三个参数，如果出错则会打印定义好的错误信息
print(b)

# fun = getattr(p,'talk')
# fun()

# print(getattr(People,'trys'))   # 反射类

# 修改对象参数
# setattr(obj,str,val)   里面有三个参数，第二个参数是要修改对象的属性参数，第三个是修改后的值
a = setattr(p, 'name', 'big')  # 实际上是与p.name='big'等效
print(p.name)
c = setattr(p, 'address', 'hanzg')  # 添加属性
print(p.address)

# setattr(People,'country','china')
# print(getattr(p,'country'))

# 删除属性
# delattr(p,'name')
# print(p.__dict__)


# # 使用例子
#
# classes Service:
#
#     def run(self):
#         while True:
#             inp = input('>>:').strip()
#             cmd = inp.split()
#             if hasattr(self,cmd[0]):
#                 func = getattr(self,cmd[0])
#                 func(cmd[1])
#
#     def get(self,cmd):
#         print('get.....',cmd)
#
#     def put(self,cmd):
#         print('put.....',cmd)
#
#
#
# obj = Service()
# obj.run()
#
# import sys
# def s1():
#     print('s1')
#
#
# def s2():
#     print('s2')
#
#
# this_module = sys.modules[__name__]
#
# a = hasattr(this_module, 's1')
# b = getattr(this_module, 's2')
# print(a)
# b()
#
#
#
