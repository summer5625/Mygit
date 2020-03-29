# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 17:20
# @Author  : XiaTian
# @File    : 面向对象可扩展性.py
# @Software: PyCharm


# 面向对象可扩展性高
# 如果新增一个类属性，将会立刻反映给所有对象，而对象却无需修改
class Chiness:
    country = 'China'  # 添加一个数据属性，所有对象都有这种属性

    def __init__(self, name, sex, age):
        self.Name = name
        self.Sex = sex
        self.Age = age

    def show_info(self):
        info = '''
        国籍：%s
        姓名：%s
        性别：%s
        年龄：%s
        ''' % (self.country, self.Name, self.Sex, self.Age)
        print(info)


p1 = Chiness('刘淑媛', '女', 23)
p2 = Chiness('夏天', '男', 23)

p1.show_info()
p2.show_info()
