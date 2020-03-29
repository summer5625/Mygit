# -*- coding: utf-8 -*-
# @Time    : 2019/3/8 22:51
# @Author  : XiaTian
# @File    : pritice.py

class Foo:
    x = 1
    def __init__(self,name):
        self.name = name

    def __getattr__(self,item):   # 这样等同于查找属性，即与用f.属性名称 方法查找对象属性，item即为对象属性名称
        print(item)
        print('属性不存在')

    def __setattr__(self, key, value):
        print('--->setattr')
        self.__dict__[key] = value
        # self.key = value               # 会无限循环下去,一直在调用自己，self.key=value触发了__setattr__

    def __delattr__(self, item):
        self.__dict__.pop(item)
        # del self.item

f = Foo('夏天')
f.a
f.cl = '光'
print(f.__dict__)


# class List(list): #继承list所有的属性，也可以派生出自己新的，比如append和mid
#     def append(self, p_object):
#         ' 派生自己的append：加上类型检查'
#         if not isinstance(p_object,int):
#             raise TypeError('must be int')
#         super().append(p_object)
#
#     @property
#     def mid(self):
#         '新增自己的属性'
#         index=len(self)//2
#         return self[index]
#
# l=List([1,2,3,4])
# # print(l)
# l.append(5)
# # print(l)
# # l.append('1111111') #报错，必须为int类型
#
# print(l.mid)
#
# #其余的方法都继承list的
# l.insert(0,-123)
# print(l)
# l.clear()
# print(l)

'''
授权：授权是包装的一个特性, 包装一个类型通常是对已存在的类型的一些定制,这种做法可以新建,修改或删除原有产品的功能。其它的则保持原样。
        授权的过程,即是所有更新的功能都是由新类的某部分来处理,但已存在的功能就授权给对象的默认属性。
        实现授权的关键点就是覆盖\_\_getattr\_\_方法
'''
# 法一
# import time
# class FileHandle:
#     def __init__(self,filename,mode='r',encoding='utf-8'):
#         self.file=open(filename,mode,encoding=encoding)
#     def write(self,line):
#         t=time.strftime('%Y-%m-%d %T')
#         self.file.write('%s %s' %(t,line))
#
#
#     def __getattr__(self, item):
#         print(item)
#         return getattr(self.file,item)
#
# f1=FileHandle('b.txt','w+')
# f1.write('你好啊')
# f1.seek(0)
# b = f1.read()  # f1.read()不存在触发__getattr__
# print(b)
# f1.close()

# 法二


# class FileHandle:
#     def __init__(self,filename,mode='r',encoding='utf-8'):
#         if 'b' in mode:
#             self.file=open(filename,mode)
#         else:
#             self.file=open(filename,mode,encoding=encoding)
#         self.filename=filename
#         self.mode=mode
#         self.encoding=encoding
#
#     def write(self,line):
#         if 'b' in self.mode:
#             if not isinstance(line,bytes):
#                 raise TypeError('must be bytes')
#         self.file.write(line)
#
#     def __getattr__(self, item):
#         print('item',item)
#         return getattr(self.file,item)
#
#     def __str__(self):
#         if 'b' in self.mode:
#             res="<_io.BufferedReader name='%s'>" %self.filename
#         else:
#             res="<_io.TextIOWrapper name='%s' mode='%s' encoding='%s'>" %(self.filename,self.mode,self.encoding)
#         return res
# f1=FileHandle('c.txt','wb')
# # f1.write('你好啊啊啊啊啊') #自定制的write,不用在进行encode转成二进制去写了,简单,大气
# f1.write('你好啊'.encode('utf-8'))
# print(f1)
# f1.close()
