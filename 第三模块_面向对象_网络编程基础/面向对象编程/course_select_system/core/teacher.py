# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 0:24
# @Author  : XiaTian
# @File    : teacher.py


class Teacher:
    '''
    定义产生老师的类
    '''

    def __init__(self, *args):
        self.teacher_name = args[0]
        self.teacher_age = args[1]
        self.school = args[2]
        self.teacher_id = args[3]
        self.teacher_course = args[4]
        self.phone = args[5]
        self.student_id = args[6]
        self.password = args[7]
        self.teacher_class = args[8]
        self.structure = self.teacher_structure(
            self.teacher_name, self.teacher_age,
            self.phone, self.school, self.password,
            self.teacher_course, self.teacher_class,
            self.student_id, self.teacher_id
        )

    def __str__(self):
        '''
        打印老师信息
        :return:
        '''
        teacher_info = '%s  %s  年龄:%s  电话:%s  课程:%s' %\
                       (
                           self.teacher_id, self.teacher_name, self.teacher_age,
                           self.phone, self.teacher_course
                       )

        return teacher_info

    @staticmethod
    def teacher_structure(*args):
        '''
        存储老师信息
        :param args:
        :return:
        '''
        data_structure = {
            'teacher_name': args[0],
            'teacher_age': args[1],
            'phone': args[2],
            'school': args[3],
            'password': args[4],
            'teacher_course': args[5],
            'teacher_class': args[6],
            'student_id': args[7],
            'teacher_id': args[8],
            'state': 0             # 账号状态标记 0：正常账号 1：账号冻结
        }

        return data_structure
