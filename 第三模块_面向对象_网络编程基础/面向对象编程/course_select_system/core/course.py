# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 0:02
# @Author  : XiaTian
# @File    : course.py


class Course:
    '''
    定义产生课程的类
    '''

    def __init__(self, *args):
        self.course_name = args[0]
        self.course_id = args[1]
        self.period = args[2]
        self.perice = args[3]
        self.course_time = args[4]
        self.course_teacher = args[5]
        self.course_state = args[6]
        self.structure = self.course_structure(
            self.course_name,
            self.course_id,
            self.period,
            self.perice,
            self.course_time,
            self.course_teacher,
            self.course_state)

    def __str__(self):
        '''
        打印课程信息
        :return:
        '''
        course_info = '%s  课程名称:%s  课程周期:%s  课程价格:%s  上课时间:%s' %\
                      (
                          self.course_id, self.course_name,
                          self.period, self.perice, self.course_time
                      )
        return course_info

    @staticmethod
    def course_structure(*args):
        '''
        创建课程信息存储结构
        :param args:
        :return:
        '''
        data_structure = {
            'course_name': args[0],
            'course_id': args[1],
            'period': args[2],
            'perice': args[3],
            'course_time': args[4],
            'course_teacher': args[5],        # 统计课程的代课老师ID，在创建教师对象时将教师ID同步过来
            'state': args[6]                  # 课程状态，1：上架  0：下架
        }

        return data_structure
