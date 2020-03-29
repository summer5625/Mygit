# -*- coding: utf-8 -*-
# @Time    : 2019/12/3  14:49
# @Author  : XiaTian
# @File    : 1_面向对象设计.py


# 第一种接口方法
# class Payment:
#     def pay(self, money):
#         raise NotImplementedError
#
#
# class Alipay(Payment):
#     pass
#
#
#
# class WechatPay(Payment):
#
#     def pay(self, money):
#         pass

"""
缺点：
    下面两个类都继承了第一个类，但是有个问题，如果在一个子类里面没有父类要求子类必须要有的方法，只要不调用该方法，
    在实例化该子类时是不会报错的
"""


# 第二种接口方法
from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        raise NotImplementedError


class Alipay(Payment):
    pass


class WechatPay(Payment):

    def pay(self, money):
        pass


"""

这种方法在父类中定义了子类必须要实现的方法，如果子类没有，在实例化子类时会直接报错，不管调用没吊用该方法

"""