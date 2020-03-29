# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 22:17
# @Author  : XiaTian
# @File    : 多态.py

# 多态：同一种事物的多种心态，即父类下面的子类：子类中与父类中相似功能，在子类中表现的不同形态
import abc
class Animal(metaclass=abc.ABCMeta): #同一类事物:动物
    # @abc.abstractmethod
    def talk(self):
        pass

class People(Animal): #动物的形态之一:人
    def talk(self):
        print('say hello')

class Dog(Animal): #动物的形态之二:狗
    def talk(self):
        print('say wangwang')

class Pig(Animal): #动物的形态之三:猪
    def talk(self):
        print('say aoao')

# 多态性：可在不考虑对象类型的情况下而直接使用对象

po1 = People()
dog1 = Dog()
pig1 = Pig()

# 动态多态性

po1.talk()
dog1.talk()
pig1.talk()

# 也可定义一个函数来使用

def func(animal):
    animal.talk()
func(po1)
func(dog1)
func(pig1)



# 鸭子类型

#二者都像鸭子,二者看起来都像文件,因而就可以当文件一样去用


class Disk:
    def read(self):
        print('disk read')
    def write(self):
        print('disk  write')

class Text:
    def read(self):
        print('text  read')

    def write(self):
        print('text  write')

disk = Disk()
text = Text()

disk.read()
disk.write()

text.read()
text.write()

print(id(disk.read))
print(id(text.read))
print(disk)
print(Text)