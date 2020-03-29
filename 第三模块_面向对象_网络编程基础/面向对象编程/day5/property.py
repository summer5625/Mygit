# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 20:56
# @Author  : XiaTian
# @File    : property.py

'''
BMI指数（bmi是计算而来的，但很明显它听起来像是一个属性而非方法，如果我们将其做成一个属性，更便于理解）

成人的BMI数值：

过轻：低于18.5

正常：18.5-23.9

过重：24-27

肥胖：28-32

非常肥胖, 高于32

体质指数（BMI）=体重（kg）÷身高^2（m）

EX：70kg÷（1.75×1.75）=22.86
'''


# class People:
#
#     def __init__(self,name,weight,height):
#         self.__name = name
#         self.weight = weight
#         self.height = height
#
#     # @property   #  一个装饰器
#     def bmi(self):
#         return self.weight/(self.height**2)
#
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,val):
#         print('setter',val)
#         if not isinstance(val,str):
#             print('名字必须是字符串')
#             return
#         self.__name = val
#
#     @name.deleter
#     def name(self):
#         print('不允许删除')
#
# people = People('夏天',62,1.68)
# # bmi = people.weight/(people.height**2)
# # print(bmi)
# # print(people.bmi())
# # print(people.bmi)                # 加了property装饰器后函数调用方式变化，不用加括号。可以像访问数据属性一样访问函数属性
#                                    # property装饰的函数必须要有返回值，其使用于需要的数据要通过计算得到的场景
#
# #people.bmi = 1.75                 # 这样直接赋值会报错
#
#
# print(people.name)                 # 查询操作
# people.name = '田'                 # 赋值操作
# people.name = 123
# del people.name                    # 删除操作
# print(people.name)


class People:

    def __init__(self,name,weight,height):
        self.__name = name
        self.weight = weight
        self.height = height

    @property
    def shut(self):
        print('show')
        return 55
    @shut.deleter
    def shut(self):
        print('deleter')
        return 55
    @shut.setter
    def shut(self,val):
        print('setter',val)

p = People('夏天',62,1.68)

print(p.shut)
p.shut = 'fffff'
del p.shut