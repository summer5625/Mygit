# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 13:28
# @Author  : XiaTian
# @File    : 自定义元类控制类的实例化.py


# # __call__方法介绍
# class Foo:
#
#     def __call__(self, *args, **kwargs):   # 定义一个__call__方法使产生对象也能被调用，如果没有__call__方法对象则不能被调用
#         print(self)
#         print(args)
#         print(kwargs)
#
# obj = Foo()
# 元类type内部也有一个__call__方法
# obj(1,2,3,a = 5,b = 6)


class Mymeta(type):     # 定义一个继承type类的元类

    def __init__(self,class_name,class_bases,class_dict):
        if not class_name.istitle():
            raise TypeError('首字母必须大写')

        if not '__doc__' in class_dict or not class_dict['__doc__'].strip():
            raise TypeError('必须有注释，且注释不能为空')


        super(Mymeta,self).__init__(class_name,class_bases,class_dict)

    def __call__(self, *args, **kwargs):
        print('触发__call__')

    # __call__方法触发后 ，进行的三部曲：
    # 1、产生一个空对象china
        obj = object.__new__(self)  #  self = Chinese
    # 2、初始化空对象china，即触发__init__方法
        self.__init__(obj,*args, **kwargs)
    # 3、返回china对象
        return obj

class Chinese(object,metaclass= Mymeta):
    '''
    中国人的类
    '''
    country = 'Chia'
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def talk(self):
        print('%s is talking' %self.name)

china = Chinese('夏天',18)
'''
     Chinese('夏天',18)=Chinese. __call__(Chinese, '夏天',18) ,Chinese可以理解为是经过Mymeta这个元类实例化得到的 一个对象
     当调用Chinese('夏天',18)时就触发了Mymeta内部的__call__方法，将Chinese传给了self，'夏天'和18传给了后面的参数。在实例化时
     会经过三个步骤：1、创建一个空对象；2、将空对象初始化，即触发__init__方法；3、有返回值
'''

print(china.__dict__)