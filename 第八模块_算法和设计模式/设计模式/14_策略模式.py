# -*- coding: utf-8 -*-
# @Time    : 2020/2/15  14:32
# @Author  : XiaTian
# @File    : 14_策略模式.py
from abc import ABCMeta, abstractmethod


class Strategy(metaclass=ABCMeta):

    @abstractmethod
    def execute(self, data):
        pass


class FastStrategy(Strategy):

    def execute(self, data):
        print("用较快的策略处理%s" % data)


class SlowStrategy(Strategy):
    def execute(self, data):
        print("用较慢的策略处理%s" % data)


class Context:

    def __init__(self, strategy, data):
        self.data = data
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def do_strategy(self):
        self.strategy.execute(self.data)


data = '去高店'
s1 = FastStrategy()
s2 = SlowStrategy()
context = Context(s1, data)
context.do_strategy()
context.set_strategy(s2)
context.do_strategy()




















