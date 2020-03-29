# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 23:23
# @Author  : XiaTian
# @File    : student.py


class Student:
    '''
    定义产生学生的类
    '''

    def __init__(self, *args):
        self.student_id = args[0]
        self.name = args[1]
        self.age = args[2]
        self.phone = args[3]
        self.student_school = args[4]
        self.student_class = args[5]
        self.password = args[6]
        self.teacher = args[7]
        self.balance = args[8]
        self.student_structure = self.student_structure(
            self.student_id, self.name, self.age,
            self.phone, self.password, self.student_school,
            self.student_class,
            self.teacher, self.balance
        )

    @staticmethod
    def student_structure(*args):
        '''
        建立学生信息存储结构
        :param args:
        :return:
        '''
        data_structure = {
            'id': args[0],
            'name': args[1],
            'age': args[2],
            'phone': args[3],
            'password': args[4],
            'school': args[5],
            'course': {},                  # 存储课程{课程ID:数}
            'class': args[6],
            'teacher': args[7],
            'balance': args[8],                       # 初始化账号余额
            'state': 0                          # 账号状态 0：为冻结 1：冻结
        }
        return data_structure

    def __str__(self):
        '''
        打印学生信息
        :return:
        '''
        student_info = '%s  %s   年龄:%s   电话:%s   学校:%s   班级:%s   余额：%s' %\
                       (
                           self.student_id, self.name, self.age, self.phone,
                           self.student_school, self.student_class, self.balance
                       )

        return student_info
