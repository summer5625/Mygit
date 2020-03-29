# -*- coding: utf-8 -*-
# @Time    : 2020/2/14  21:07
# @Author  : XiaTian
# @File    : 8_桥模式.py
from abc import ABCMeta, abstractmethod


class Shape(metaclass=ABCMeta):

    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass


class Color(metaclass=ABCMeta):

    @abstractmethod
    def paint(self, shape):
        pass


class Rectangle(Shape):

    name = '长方形'
    def draw(self):
        self.color.paint(self)


class Circle(Shape):
    name = "圆形"
    def draw(self):
        # 圆形逻辑
        self.color.paint(self)


class Line(Shape):
    name = "直线"
    def draw(self):
        # 直线逻辑
        self.color.paint(self)


class Red(Color):
    def paint(self, shape):
        print("红色的%s" % shape.name)


class Green(Color):
    def paint(self, shape):
        print("绿色的%s" % shape.name)


class Blue(Color):
    def paint(self, shape):
        print("蓝色的%s" % shape.name)



shape = Line(Blue())
shape.draw()

ss = Circle(Green())
ss.draw()












