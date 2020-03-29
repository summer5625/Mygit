# -*- coding: utf-8 -*-
# @Time    : 2020/2/14  15:33
# @Author  : XiaTian
# @File    : 3.工厂方法模式.py
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


class BankPay(Payment):
    def pay(self, money):
        print("银行卡支付%d元." % money)


class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass


class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay()


class WechatPayFactory(PaymentFactory):
    def create_payment(self):
        return WechatPay()


class HuabeiFactory(PaymentFactory):
    def create_payment(self):
        return Alipay(use_huabei=True)


class BankPayFactory(PaymentFactory):
    def create_payment(self):
        return BankPay()


# client

pf = HuabeiFactory()
p = pf.create_payment()
p.pay(100)
