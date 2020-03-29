# -*- coding: utf-8 -*-
# @Time    : 2019/3/4 20:06
# @Author  : XiaTian
# @File    : 组合.py


# 定义人类
class People:
    school = 'luffycity'

    def __init__(self, name, sex, age):
        self.name = name
        self.age = age
        self.sex = sex


# 定义老师类
class Teacher(People):

    def __init__(self, name, sex, age, level, salary):
        super().__init__(name, sex, age)
        self.level = level
        self.salary = salary


# 定义学生类
class Student(People):

    def __init__(self, name, sex, age, class_time):
        super().__init__(name, sex, age)
        self.class_time = class_time


# 定义学生类
class Course:

    def __init__(self, course_name, course_price, course_period):
        self.course_name = course_name
        self.course_price = course_price
        self.course_period = course_period

    def course_info(self):
        info = '''
                    课程：%s
                    价格：%s
                    时长：%s        
            ''' % (self.course_name, self.course_price, self.course_period)
        print(info)


class Data:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def data_info(self):
        print('%s-%s-%s' % (self.year, self.month, self.day))


teacher1 = Teacher('刘淑', '女', 26, 50, 10000)  # 实例化老师类对象
teacher2 = Teacher('夏天', '男', 28, 70, 20000)

student1 = Student('王战', '男', 30, '07:30:00')
student2 = Student('狗熊', '男', 30, '09:30:00')  # 实例化学生类对象

python = Course('python', 12000, '6 months')  # 实例化课程类对象
linux = Course('linux', 8000, '5 months')

data = Data(1993, 5, 16)

student1.course = python
student2.course1 = python
student2.course2 = linux
# student2.course1.course_info()                 # 将课程对象组合到学生对象中：组合是两个对象的关系为 xx 有 xx
student1.datas = data
# student1.datas.data_info()
print(id(student2.course1))
print(id(python))
