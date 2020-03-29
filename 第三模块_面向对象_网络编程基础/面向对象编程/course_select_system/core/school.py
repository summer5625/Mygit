# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 0:23
# @Author  : XiaTian
# @File    : school.py


import pickle

from conf import setting


class School:
    '''
    定义产生学校的类
    '''

    def __init__(self, *args):
        self.school_id = args[0]
        self.address = args[1]
        self.name = '%s校区' % self.address
        self.course_id = args[2]
        self.teacher_id = args[3]
        self.student_id = args[4]
        self.structure = self.structure(
            self.school_id,
            self.name,
            self.course_id,
            self.teacher_id,
            self.student_id)

    @staticmethod
    def structure(*args):
        '''
        构建学校信息存储结构
        :param args:
        :return:
        '''
        data_structure = {
            'school_id': args[0],
            'school_name': args[1],
            'course_id': args[2],
            'teacher_id': args[3],
            'student_id': args[4],
        }
        return data_structure

    def __str__(self):
        '''
        打印学校信息
        :return:
        '''
        account_path = r'%s\db\%s\%s.pkl' % (
            setting.FILE_PATH, 'course', 'course')
        f = open(account_path, 'rb')
        course_data = pickle.load(f)
        f.close
        course_list = []
        for i in self.course_id:
            course_list.append(course_data[i])

        school_info = '%s  %s  开设课程:%s  师资力量:%s名老师  在校学生:%s人' % (
            self.school_id, self.name, course_list, len(self.teacher_id), len(self.student_id))
        return school_info
