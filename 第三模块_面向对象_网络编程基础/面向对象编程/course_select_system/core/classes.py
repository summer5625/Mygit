# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 0:30
# @Author  : XiaTian
# @File    : classes.py


class Class:
    '''定义产生班级的类'''

    def __init__(self, *args):
        self.class_name = args[0]
        self.class_id = args[1]
        self.class_students = args[2]
        self.school = args[3]
        self.class_teacher = args[4]
        self.class_volumetric = args[5]      # 班级容量
        self.structure = self.class_structure(
            self.class_name, self.class_id, self.school,
            self.class_students, self.class_teacher,
            self.class_volumetric
        )

    def __str__(self):
        class_info = '%s  %s  班级人数:%s  班级容量:%s' % (
            self.class_id, self.class_name, len(self.class_students), self.class_volumetric)
        return class_info

    @staticmethod
    def class_structure(*args):
        '''
        存储课程信息
        :param args:
        :return:
        '''
        data_structure = {
            'class_name': args[0],
            'class_id': args[1],
            'school': args[2],
            'class_students': args[3],
            'class_teacher': args[4],
            'class_volumetric': args[5],
            'class_course': None
        }
        return data_structure
