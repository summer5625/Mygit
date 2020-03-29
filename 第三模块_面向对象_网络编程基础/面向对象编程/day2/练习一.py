# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 17:42
# @Author  : XiaTian
# @File    : 练习一.py

# 课堂练习一
'''
编写一个产生学生的类，产生一堆学生对象
要求：
    有一个计数器（属性），统计总共产生多少个对象
'''

class Students:

    school = 'luffycity'
    count = 0
    def __init__(self,name,sex,age,class_number):
        self.Name = name
        self.Sex = sex
        self.Age = age
        self.Class = class_number
        # self.count += 1                 # 这样操作只对每个的对象的count加了1，并没有将类里面的count加1，操作的是每个对象的count
        Students.count += 1               # 这样操作才是操作类中的名称空间中的count
    def hobby(self,appetites):
        print('%s hobby is %s'%(self.Name,appetites))


stu1 = Students('刘淑媛','女',23,'python二班')
stu2 = Students('夏天','男',25,'python二班')

print(stu1.count)
print(stu2.count)

