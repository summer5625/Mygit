# -*- coding: utf-8 -*-
# @Time    : 2020/2/14  15:21
# @Author  : XiaTian
# @File    : 2.简单工厂模式.py
from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    # abstract class
    @abstractmethod
    def pay(self, money):
        pass

class Alipay(Payment):
    def __init__(self, use_huabei=False):
        self.use_huaei = use_huabei

    def pay(self, money):
        if self.use_huaei:
            print("花呗支付%d元." % money)
        else:
            print("支付宝余额支付%d元." % money)


class WechatPay(Payment):
    def pay(self, money):
        print("微信支付%d元." % money)


# 创建工厂类
class PaymentFactory:

    def create_payment(self, method):

        if method == 'alipay':
            return Alipay()
        elif method == 'wechat':
            return WechatPay()
        else:
            raise TypeError('No such payment name %s' % method)

'''

不需要暴露实现细节，通过一个工厂来提供统一的一个简单的接口来实现用户功能

'''




















