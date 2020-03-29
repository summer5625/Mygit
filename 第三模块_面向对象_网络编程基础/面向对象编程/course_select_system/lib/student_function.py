# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 1:29
# @Author  : XiaTian
# @File    : student_function.py

import re

from core.modules import Module
from conf import setting
from core.logger import Logger
from core import landing


class Student_Function(Module):
    '''
        学生角色拥有的功能
    '''

    @classmethod
    def make_student(cls):
        '''
        注册新账号
        :return:
        '''
        new_student = cls.create_student()                 # 创建新的学生对象
        choice_school = cls.select_school()                # 注册时选择学校
        choice_course = cls.select_course(
            'course', choice_school)        # 注册时选择课程
        choice_teacher = cls.select_teacher(
            choice_course, choice_school)  # 注册时选择老师
        choice_class = cls.select_class(
            choice_teacher)                   # 注册时选择班级
        new_student.student_structure['school'] = choice_school
        new_student.student_structure['teacher'] = choice_teacher
        new_student.student_structure['class'] = choice_class
        new_student.student_structure['id'] = cls.creat_id(
            'student', choice_school, choice_class)  # 生成学号
        # 选课后分数为0
        new_student.student_structure['course'][choice_course] = 0
        student_list = cls.get_data('student', 'student')
        student_list[new_student.student_structure['id']] = new_student.name
        cls.save_file('student', 'student', student_list)
        cls.save_file(
            'student',
            new_student.student_structure['id'],
            new_student.student_structure)  # 保存信息
        print('注册成功!')
        print('您的序号为%s，请保管好号码，用以登陆!' % new_student.student_structure['id'])
        log_msg = 'role:%s   account:%s   operation:register   info:注册成功!' %\
                  ('student', new_student.student_structure['id'])
        loggers = Logger.logs('student')
        # 报存注册日志
        loggers.info(log_msg)

        massage_school = cls.get_data('school', choice_school)
        massage_school['student_id'].append(
            new_student.student_structure['id'])
        cls.save_file('school', choice_school, massage_school)    # 同步学生信息给学校

        massage_teacher = cls.get_data('teacher', choice_teacher)
        massage_teacher['student_id'].append(
            new_student.student_structure['id'])
        cls.save_file('teacher', choice_teacher, massage_teacher)  # 同步学生信息给老师

        massage_class = cls.get_data('classes', choice_class)
        massage_class['class_students'].append(
            new_student.student_structure['id'])
        cls.save_file('classes', choice_class, massage_class)      # 同步学生信息给班级

    @classmethod
    def choice_course(cls, role, account):
        '''
        购买课程
        :param account:
        :return:
        '''
        massage = cls.get_data(role, account)
        course_id = cls.select_course(role, massage['school'])
        course_msg = cls.get_data('course', course_id)
        if int(massage['balance']) >= int(course_msg['perice']):
            massage['balance'] = int(
                massage['balance']) - int(course_msg['perice'])
            massage['course'][course_id] = None
            cls.save_file(role, account, massage)
            log_msg = 'role:student   account:%s   operation:choice course   info:%s课程选课成功!' %\
                      (account, course_id)
            loggers = Logger.logs(role)
            loggers.info(log_msg)

        else:
            print('余额不足，请充值!')

    @classmethod
    def recharge(cls, role, account):
        '''
        余额充值
        :param account:
        :return:
        '''
        massage = cls.get_data(role, account)
        money = input('充值金额(b退出)>>:').strip()
        if money == 'b':
            return
        if money.isdigit():
            money = int(money)
            massage['balance'] = int(massage['balance']) + money
            cls.save_file(role, account, massage)
            log_msg = 'role:student  account:%s  operation:recharge  info:成功充值%s元!' %\
                      (account, money)
            loggers = Logger.logs(role)
            loggers.info(log_msg)                                 # 记录充值信息

    @classmethod
    def show_massage(cls, role, account):
        '''
        打印账号信息
        :param account:
        :return:
        '''
        my_account = cls.born_student(role, account)
        print(my_account)

    @classmethod
    def look_score(cls, role, account):
        '''
        查看课程分数
        :param account:
        :return:
        '''
        massage = cls.get_data(role, account)
        course_msg = cls.get_data('course', 'course')
        for k, v in massage['course'].items():
            print(course_msg[k], v)

    @classmethod
    def recharge_record(cls, role, account):
        '''
        查看充值记录
        :param account:
        :return:
        '''
        log_path = r'%s\log\%s.log' % (setting.FILE_PATH, role)
        f = open(log_path, 'r', encoding='utf-8')
        lines = f.readlines()
        f.close()
        key = 'account:%s' % account
        for i in lines:
            if re.search(
                    key,
                    i) and re.search(
                    'operation:recharge',
                    i):         # 匹配出该账户充值日志
                a = re.split(r':|\s', i)
                print(a[0], a[18])

    @classmethod
    def chang_massage(cls, role, account):
        '''
        更新个人信息
        :param account:
        :return:
        '''
        old_massage = cls.get_data(role, account)
        cls.update_student(role, account)
        new_massage = cls.get_data(role, account)
        if str(old_massage) == str(new_massage):                # 判断信息是否修改过
            log_msg = 'role:student   account:%s   operation:update massage   info:个人信息更新成功!' % \
                      (account)
            loggers = Logger.logs(role)
            loggers.info(log_msg)                               # 记录学生信息修改记录

    @classmethod
    def update_password(cls, role, account):
        cls.change_password(role, account)
        log_msg = 'role:student   account:%s   operation:change password   info:密码修改成功!' % (
            account)
        loggers = Logger.logs(role)
        loggers.info(log_msg)


def function_control(role):
    '''
    功能分发
    :param role:
    :return:
    '''
    function = [
        ['退出', exit],
        ['选课', Student_Function.choice_course],
        ['充值', Student_Function.recharge],
        ['个人信息查询', Student_Function.show_massage],
        ['分数查看', Student_Function.look_score],
        ['充值记录查询', Student_Function.recharge_record],
        ['个人信息修改', Student_Function.chang_massage],
        ['密码修改', Student_Function.update_password]
    ]
    account = landing.landing(role)         # 获取用户登录时的账号
    if account:                             # 确定用户是否登录成功
        flag = True
    else:
        flag = False
    while flag:
        for index, i in enumerate(function):
            print(index, i[0])
        choice = input('请输入操作序号>>:').strip()
        if choice.isdigit():
            choice = int(choice)
        else:
            print('请输入正确数字序号!')
            continue
        if choice == 0:
            exit()
        elif 0 < choice < len(function):
            function[choice][1](role, account)
        else:
            print('请输入正确的序号!')


def main(role):
    '''
    学生程序入口
    :param role:
    :return:
    '''
    operation = [
        ['注册', Student_Function.make_student],
        ['登陆', function_control]
    ]
    for index, i in enumerate(operation):
        print(index, i[0])
    choice = input('输入操作序号>>:').strip()
    if choice.isdigit():
        choice = int(choice)
    else:
        print('输入不合法!')
        exit()
    if choice == 0:
        Student_Function.make_student()
        function_control(role)
    elif choice == 1:
        function_control(role)
    else:
        print('输入不合法!')
        exit()
