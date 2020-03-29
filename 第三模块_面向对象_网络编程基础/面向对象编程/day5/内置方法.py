# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 21:10
# @Author  : XiaTian
# @File    : 内置方法.py


# __getitem__,__setitem__,__delitem__:此系列相当于将对象或者类的属性名称和对应的值对应起来，形成像字典的结构，

class Foo:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def func(self):
        print('from func')

    def __getitem__(self, item):
        print('getattr><')

        return self.__dict__[item]  # 当输入的不是字典中的key时会报错
        # return self.__dict__.get(item)    # 当输入的不是字典中的key时不会报错

    def __setitem__(self, key, value):
        print('setattr><')
        print(key, value)
        self.__dict__[key] = value

    def __delitem__(self, key):
        print('delitem><')
        # del self.__dict__[key]
        self.__dict__.pop(key)


f = Foo('夏天', 25)

# print(Foo.__dict__)
print(f.__dict__)
print(f['age'])

f['name'] = 'tiantian'
print(f.name)
f['sex'] = 'man'
print(f.sex)

del f['name']
print(f.__dict__)

# __str__方法：打印对象时可以定制需要打印对象的那些信息，


# classes Foo:
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):   # 会在打印对象时触发此方法
#         print('str><')
#         return 'name:%s  age:%s'%(self.name,self.age)  # __str__方法必须要有返回值，返回值必须是字符串
# f = Foo('夏天',18)
# print(f)                        # 打印对象是直接打印定制化的输出

# python在程序运行完成后会自动回收程序内定义的名称空间资源，不会回收申请的操作系统资源
# __del__:回收和对象相关连的资源，如：申请的操作系统资源

# class Open:
#
#     def __init__(self,filename):
#         print('open file...')
#         self.filename = filename
#
#     def __del__(self):          # 在不调用此方法时，在程序结束后会自动触发，回收与对象相关的资源。
#         print('回收资源....')    # 相当于文件操作中的f.clos()
#
#
# f = Open('setting.py')
# del f
# print('---finish----')
