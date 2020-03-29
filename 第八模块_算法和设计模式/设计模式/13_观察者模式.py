# -*- coding: utf-8 -*-
# @Time    : 2020/2/15  13:53
# @Author  : XiaTian
# @File    : 13_观察者模式.py
from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):

    @abstractmethod
    def update(self, notice):
        pass


class Notice:

    def __init__(self):
        self.observers = []

    def attach(self, obs):
        self.observers.append(obs)

    def detach(self, obs):
        self.observers.remove(obs)

    def notify(self):
        for obs in self.observers:
            obs.update(self)


class StaffNotice(Notice): # 具体发布者

    def __init__(self, company_info=None):
        super().__init__()
        self.__company_info = company_info

    @property
    def company_info(self):
        return self.__company_info

    @company_info.setter
    def company_info(self, info):
        self.__company_info = info
        self.notify()  # 推送


class Staff(Observer):

    def __init__(self):
        self.company_info = None

    def update(self, notice):
        self.company_info = notice.company_info


notice = StaffNotice('初始化公司了')
s1 = Staff()
s2 = Staff()
notice.attach(s1)
notice.attach(s2)
notice.company_info = '发奖金喽'
print(s1.company_info)
print(s2.company_info)
notice.detach(s2)
notice.company_info = '放假了'
print(s1.company_info)
print(s2.company_info)



































