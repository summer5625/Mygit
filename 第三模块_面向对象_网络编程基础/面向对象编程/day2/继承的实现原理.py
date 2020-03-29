# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 21:55
# @Author  : XiaTian
# @File    : 继承的实现原理.py


class A:
    def text(self):
        print('from A')


class B(A):
    # def text(self):
    #     print('from B')
    pass

class C(A):
    # def text(self):
    #     print('from C')
    pass

class D(B):
    # def text(self):
    #     print('from D')
    pass

class E(B):
    # def text(self):
    #     print('from E')
    pass

class F(C):
    # def text(self):
    #     print('from F')
    pass

class G(C):
    # def text(self):
    #     print('from G')
    pass

class H(D,E):
    # def text(self):
    #     print('from H')
    pass
class I(F,G):
    # def text(self):
    #     print('from I')
    pass

class J(H,I):
    # def text(self):
    #     print('from J')
    pass

a = J()
print(J.mro())
a.text()
