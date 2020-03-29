# -*- coding: utf-8 -*-
# @Time    : 2020/2/15  14:47
# @Author  : XiaTian
# @File    : 15_模板方法模式.py
from abc import ABCMeta, abstractmethod
from time import sleep


class Window(metaclass=ABCMeta):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def repaint(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def run(self):

        self.start()
        while True:
            try:
                self.repaint()
                sleep(1)
            except KeyboardInterrupt:
                break
        self.stop()


class MyWindow(Window):

    def __init__(self, msg):
        self.msg = msg

    def start(self):
        print("窗口开始运行")

    def stop(self):
        print("窗口结束运行")

    def repaint(self):
        print(self.msg)


MyWindow('Yes...').run()






















