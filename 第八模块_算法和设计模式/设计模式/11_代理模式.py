# -*- coding: utf-8 -*-
# @Time    : 2020/2/15  12:56
# @Author  : XiaTian
# @File    : 11_代理模式.py
from abc import ABCMeta, abstractmethod


class Subject(metaclass=ABCMeta):

    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self):
        pass


class RealSubject(Subject):

    def __init__(self, filename):
        self.filename = filename
        f = open(filename, 'r', encoding='utf-8')
        print('读取文件内容')
        self.content = f.read()
        f.close()

    def get_content(self):
        return self.content

    def set_content(self, content):
        f = open(self.filename, 'w', encoding='utf-8')
        f.write(content)
        f.close()


class VirtualProxy(Subject):

    def __init__(self, filename):
        self.filename = filename
        self.subj = None

    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()

    def set_content(self, content):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.set_content(content)


class ProtectedProxy(Subject):

    def __init__(self, filename):
        self.subj = RealSubject(filename)

    def get_content(self):
        self.subj.get_content()

    def set_content(self, content):
        raise PermissionError('无写入权限')


sub = RealSubject('test.txt')
print(sub.get_content())

s = ProtectedProxy('test.txt')
print(s.get_content())
s.set_content('aaa')


















