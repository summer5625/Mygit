# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 0:41
# @Author  : XiaTian
# @File    : 定制元类控制类的行为.py


class Mymeta(type):  # 定义一个继承type类的元类

    def __init__(self, class_name, class_bases, class_dict):
        if not class_name.istitle():
            raise TypeError('首字母必须大写')  # raise抛异常关键字，有异常程序运行到此就结束了
        print(class_dict)  # 查看类的名称空间
        if not '__doc__' in class_dict or not class_dict['__doc__'].strip():  # 控制创建类的行为
            raise TypeError('必须有注释，且注释不能为空')

        super(Mymeta, self).__init__(class_name, class_bases, class_dict)  # 创建类的三要素


class Chinese(object, metaclass=Mymeta):  # metaclass= Mymeta表示定义了Chinese的元类是Mymeta
    '''
    中国人的类
    '''
    country = 'Chia'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print('%s is talking' % self.name)
