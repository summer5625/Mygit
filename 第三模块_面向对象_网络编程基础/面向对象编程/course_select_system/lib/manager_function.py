# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 1:28
# @Author  : XiaTian
# @File    : manager_function.py

from core.modules import Module
from core.logger import Logger
from core import landing


class Manager_Function(Module):

    @classmethod
    def make_school(cls):
        '''
        添加学校
        :return:
        '''
        new_school = cls.creat_school()   # 创建学校对象
        pick_course_id = cls.select_course(
            'school', new_school.school_id)   # 绑定课程到学校
        for i in pick_course_id:                                            # 经课程id添加到学校
            new_school.structure['course_id'].append(i)
        cls.save_file(
            'school',
            new_school.school_id,
            new_school.structure)  # 保存学校信息
        log_msg = 'role:admin   account:admin   operation:creat school   info:%s创建成功！' % new_school.name
        loggers = Logger.logs('manager')
        loggers.info(log_msg)

    @classmethod
    def make_class(cls):
        '''
        添加班级
        :return:
        '''
        new_class = cls.creat_class()                             # 创建班级
        choice_school = cls.select_school()                        # 给学校绑定班级
        choice_course = cls.select_course('course', choice_school)  # 给班级绑定课程
        choice_teacher = cls.select_teacher(
            choice_course, choice_school)        # 给班级绑定老师
        new_class.structure['school'] = choice_school
        new_class.structure['class_course'] = choice_course
        new_class.structure['class_teacher'] = choice_teacher
        cls.save_file(
            'classes',
            new_class.class_id,
            new_class.structure)   # 保存班级信息

        massage_teacher = cls.get_data('teacher', choice_teacher)
        massage_teacher['teacher_class'].append(new_class.class_id)
        cls.save_file(
            'teacher',
            choice_teacher,
            massage_teacher)         # 班级信息同步到老师

        log_msg = 'role:admin   account:admin   operation:creat class   info:%s创建成功' % new_class.class_name
        loggers = Logger.logs('manager')
        loggers.info(log_msg)

    @classmethod
    def make_teacher(cls):
        '''
        添加老师账户
        :return:
        '''
        new_teacher = cls.creat_teacher()                         # 创建老师对象
        choice_school = cls.select_school()                       # 选择学校
        choice_course = cls.select_course('course', choice_school)  # 选择课程
        new_teacher.structure['school'] = choice_school
        new_teacher.structure['teacher_course'] = choice_course
        new_teacher.structure['teacher_id'] = cls.creat_id(
            'teacher', choice_school,
            new_teacher.structure['teacher_class']
        )                               # 生成老师ID
        teacher_list = cls.get_data('teacher', 'teacher')
        teacher_list[new_teacher.structure['teacher_id']
                     ] = new_teacher.teacher_name
        cls.save_file('teacher', 'teacher', teacher_list)
        cls.save_file(
            'teacher',
            new_teacher.structure['teacher_id'],
            new_teacher.structure)  # 报存老师信息

        massage_course = cls.get_data('course', choice_course)
        massage_course['course_teacher'].append(
            new_teacher.structure['teacher_id'])
        print(massage_course)
        cls.save_file('course', choice_course, massage_course)    # 同步教师信息给课程

        massage_school = cls.get_data('school', choice_school)
        massage_school['teacher_id'].append(
            new_teacher.structure['teacher_id'])
        cls.save_file('school', choice_school, massage_school)   # 同步老师信息到学校

        log_msg = 'role:admin   account:admin   operation:creat teacher   info:%s账户创建成功' \
                  % new_teacher.structure['teacher_id']
        loggers = Logger.logs('manager')
        loggers.info(log_msg)

    @classmethod
    def make_course(cls):
        '''
        添加新课程
        :return:
        '''
        new_course = cls.creat_course()
        log_msg = 'role:admin   account:admin   operation:creat course   info:%s课程创建成功' \
                  % new_course.course_name
        loggers = Logger.logs('manager')
        loggers.info(log_msg)

    @classmethod
    def change_course(cls):
        '''
        更新课程信息
        :return:
        '''
        course = cls.update_course('course')
        log_msg = 'role:admin   account:admin   operation:update course   info:%s课程更新成功!' % course
        loggers = Logger.logs('manager')
        loggers.info(log_msg)

    @classmethod
    def replacement(cls):
        '''
        重置账号状态
        :return:
        '''
        role_list = [['老师账户重置', 'teacher'], ['学生账户重置', 'student']]
        while True:
            for index, i in enumerate(role_list):
                print(index, i[0])
            choice = input('输出操作序号(b退出)>>:').strip()
            if choice == 'b':
                return
            if choice.isdigit():
                choice = int(choice)
            else:
                print('请输入正确的序号!')
                return
            if len(role_list) >= choice:
                account = input('请输入要重置的账号>>:').strip()
                account_list = cls.get_data(
                    role_list[choice][1], role_list[choice][1])
            else:
                print('请输入正确的序号!')
                return
            if account in account_list:
                cls.reset(role_list[choice][1], account)
                log_msg = 'role:admin   account:admin   operation:reset   info:%s:%s账户重置成功!' %\
                          (role_list[choice][1], account)
                loggers = Logger.logs('manager')
                loggers.info(log_msg)


@landing.manager_landing
def main():
    '''
    管理员功能分发
    :return:
    '''
    function = [
        ['退出', exit],
        ['学校创建', Manager_Function.make_school],
        ['课程创建', Manager_Function.make_course],
        ['班级创建', Manager_Function.make_class],
        ['添加老师', Manager_Function.make_teacher],
        ['更新课程', Manager_Function.change_course],
        ['重置状态', Manager_Function.replacement]
    ]
    while True:
        for index, i in enumerate(function):
            print(index, i[0])
        choice = input('请输入操作序号>>:').strip()
        if choice.isdigit():
            choice = int(choice)
        else:
            print('请输入正确的序号!')
            return
        if choice < len(function):
            function[choice][1]()
        else:
            print('请输入正确的序号!')
