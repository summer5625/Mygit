# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 21:44
# @Author  : XiaTian
# @File    : 抽象类.py

# 导入abc模块实现抽象类
import abc

# 定义抽象类，抽象类不能被实例化
class Animal(metaclass = abc.ABCMeta):

    all_type = 'animal'

    @abc.abstractmethod
    def run(self):
        pass

    @abc.abstractmethod
    def eat(self):
        pass

    @abc.abstractmethod
    def sleep(self):
        pass


class People(Animal):                # 定义类的抽象父类有的相似属性，在子类中都必须定义，否则会报错

    def run(self):                   # 功能属性的命名必须与抽象类中对应功能属性名称相同
        print('peopel is running')

    def eat(self):
        print('people is eating')

    def sleep(self):
        print('people is sleeping ')

class Pig(Animal):

    def run(self):
        print('pig is running')

    def eat(self):
        print('pig is eating')

    def sleep(self):
        print('pig is sleeping')


people = People()
pig = Pig()

people.run()
people.eat()
people.sleep()

pig.run()
pig.eat()
pig.sleep()

a = Animal()