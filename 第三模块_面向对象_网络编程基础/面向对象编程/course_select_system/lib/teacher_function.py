# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 1:29
# @Author  : XiaTian
# @File    : teacher_function.py


from core.modules import Module
from core.logger import Logger
from core import landing


class Teacher_Function(Module):
    '''
    老师角色功能
    '''

    @staticmethod
    def play_score(role, account):
        '''
        给学生打分
        :param account:
        :return:
        '''
        while True:
            teacher_msg = Teacher_Function.get_data(role, account)
            for i in teacher_msg['student_id']:
                student = Teacher_Function.born_student('student', i)
                print(student)
            student_id = input('输入学生学号(b退出)>>:').strip()
            if student_id == 'b':
                return
            if student_id in teacher_msg['student_id']:
                student_msg = Teacher_Function.get_data('student', student_id)
                score = input('课程分数>>:').strip()
                student_msg['course'][teacher_msg['teacher_course']] = score
                Teacher_Function.save_file('student', student_id, student_msg)
            else:
                print('%s不是你的学生!' % student_id)

    @staticmethod
    def schooltime(role, account):
        '''
        老师上课打卡
        :param account:
        :return:
        '''
        while True:
            teacher_msg = Teacher_Function.get_data(role, account)
            print(teacher_msg)
            for i in teacher_msg['teacher_class']:
                class_msg = Teacher_Function.born_class('classes', i)
                print(class_msg)
            class_id = input('请输入要上课班级的代号(b退出)>>:').strip()   # 选择上课班级

            if class_id in teacher_msg['teacher_class']:
                log_msg = 'role:teacher   account:%s   operation:schooltime   info:已在%s班级上课!' %\
                          (account, class_id)
                loggers = Logger.logs(role)
                loggers.info(log_msg)                      # 记录老师上课记录
                return
            else:
                print('请输入正确班级代码!')

    @staticmethod
    def look_class(role, account):
        '''
        查看班级学员信息
        :param account:
        :return:
        '''
        massage = Teacher_Function.get_data(role, account)
        while True:
            for i in massage['teacher_class']:
                class_msg = Teacher_Function.born_class('classes', i)
                print(class_msg)
            class_id = input('输入要查询班级的代码(b退出)>>:').strip()
            if class_id == 'b':
                return
            if class_id in massage['teacher_class']:
                class_msg = Teacher_Function.get_data('classes', class_id)
                class_obj = Teacher_Function.born_class('classes', class_id)
                print(class_obj)                                     # 查看班级信息
                for i in class_msg['class_students']:
                    student_obj = Teacher_Function.born_student('student', i)
                    student_msg = Teacher_Function.get_data('student', i)
                    show_msg = '学号:%s  姓名:%s  课程:%s  分数:%s' %\
                               (student_obj.student_id, student_obj.name, massage['teacher_course'],
                                student_msg['course'][massage['teacher_course']])
                    print(show_msg)                                 # 查看学员信息
                    continue
            else:
                print('请输入正确班级代码!')
                continue

    @staticmethod
    def chang_massage(role, account):
        '''
        更新个人信息
        :param account:
        :return:
        '''
        old_massage = Teacher_Function.get_data(role, account)
        Teacher_Function.update_teacher(role, account)
        new_massage = Teacher_Function.get_data(role, account)
        if str(old_massage) == str(new_massage):       # 判断信息是否修改过
            log_msg = 'role:teacher   account:%s   operation:update massage   info:个人信息更新成功!' %\
                      (account)
            loggers = Logger.logs(role)
            loggers.info(log_msg)                      # 记录老师信息修改记录

    @staticmethod
    def update_password(role, account):
        Teacher_Function.change_password(role, account)
        log_msg = 'role:teacher   account:%s   operation:change password   info:密码修改成功!' % (
            account)
        loggers = Logger.logs(role)
        loggers.info(log_msg)


def main(role):
    '''
    老师功能分发
    :param role:
    :return:
    '''
    function = [
        ['退出', exit],
        ['个人信息修改', Teacher_Function.chang_massage],
        ['密码修改', Teacher_Function.update_password],
        ['班级查看', Teacher_Function.look_class],
        ['上课打卡', Teacher_Function.schooltime],
        ['打分', Teacher_Function.play_score]
    ]                                                      # 功能列表
    # 获取用户登录时的账号
    account = landing.landing(role)
    if account:                                                       # 确定用户是否登录成功
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
            print('请输入正确的操作序号!')
            continue
        if choice == 0:
            exit()
        if 0 < choice < len(function):
            function[choice][1](role, account)
        else:
            print('请输入正确的操作序号!')
