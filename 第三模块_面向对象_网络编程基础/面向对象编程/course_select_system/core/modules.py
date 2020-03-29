# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 0:21
# @Author  : XiaTian
# @File    : modules.py

import pickle
import time
import os
import hashlib
import sys

from conf import setting
from core.school import School
from core.course import Course
from core.teacher import Teacher
from core.student import Student
from core.classes import Class


class Module:

    @staticmethod
    def save_file(role, account_id, data):
        '''
            保存用户数据
        :param role: 用户角色
        :param account_id: 账户id
        :param data: 账户数据
        :return:
        '''

        file_path = r'%s\db\%s\%s.pkl' % (setting.FILE_PATH, role, account_id)
        f = open(file_path, 'wb')
        pickle.dump(data, f)
        f.close()

    @staticmethod
    def creat_id(role, school_id, class_id):
        '''
        生成角色ID
        :param role: 角色
        :param school_id: 学校ID
        :param class_id: 班级ID
        :return:
        '''
        enter_time = time.strftime('%Y', time.localtime())         # 获取注册时间+
        if role == 'teacher':
            data_1 = Module.get_data('school', school_id)
            suffix_int = len(data_1['teacher_id']) + 1
            # print(suffix_int)
            suffix_1 = '%04d' % suffix_int
            # print(suffix_1)
            new_id = enter_time + str(school_id) + suffix_1  # 生成老师ID
            # print(new_id)
        elif role == 'student':
            # data_2 = Module.get_data('student','student')
            class_data = Module.get_data('classes', class_id)

            suffix_int1 = len(class_data['class_students']) + 1
            suffix_2 = '%03d' % suffix_int1
            new_id = enter_time + str(school_id) + \
                str(class_id) + suffix_2   # 生成学生ID
        return new_id

    @staticmethod
    def get_data(role, account_id):
        '''
        读取用户信息
        :param role: 用户角色
        :param account_id: 用户ID
        :return:
        '''
        account_path = r'%s\db\%s\%s.pkl' % (
            setting.FILE_PATH, role, account_id)
        f = open(account_path, 'rb')
        account_data = pickle.load(f)
        f.close()

        return account_data

    @staticmethod
    def encrypt(data):
        '''
        给密码加密
        :param data:
        :return:
        '''
        m_pwd = hashlib.md5()
        m_pwd.update(data.encode())
        t_pwd = m_pwd.hexdigest()

        return t_pwd

    @staticmethod
    def check_file(role, file_name):
        '''
        检查是文件是否存在
        :param role:
        :param file_name:
        :return:
        '''
        file_path = r'%s\db\%s\%s.pkl' % (setting.FILE_PATH, role, file_name)

        return os.path.exists(file_path)

    @staticmethod
    def creat_school():
        '''
        创建新学校
        :return:
        '''
        while True:

            address = input('学校地址>>:').strip()
            school_name = '%s校区' % address
            # 获取所有学校列表{'school_name':school_id}
            school_list = Module.get_data('school', 'school')
            if school_name == 'b':
                return
            if (school_name not in school_list.values()) and (
                    len(address) != 0):  # 判断学校命名是否合法
                data = Module.get_data('school', 'school')
                school_id = '%03d' % (len(data) + 1)            # 生成学校ID
                obj = School(school_id, address, [], [], [])       # 生成学校对象
                school_list[school_id] = school_name
                Module.save_file(
                    'school', school_id, obj.structure)   # 存储新建学校信息
                # 将新建学校ID添加进学校列表{ID:name}
                Module.save_file('school', 'school', school_list)
                return obj
            else:
                print('地址有重复或者为空!')

    @staticmethod
    def born_school(role, ID):
        '''
        从文件中读取参数实例化学校
        :param role:
        :param ID:
        :return:
        '''
        school_data = Module.get_data(role, ID)
        school = School(
            school_data['school_id'],
            school_data['school_name'],
            school_data['course_id'],
            school_data['teacher_id'],
            school_data['student_id']
        )
        return school

    @staticmethod
    def show_school(role):
        massage = Module.get_data(role, role)          # massage结构为{name:ID}
        for k in massage.keys():
            school = Module.born_school(role, k)
            print(school)                             # 打印所有学校信息

    @staticmethod
    def creat_course():
        '''
        创建课程
        :return:
        '''
        while True:

            course_list = Module.get_data('course', 'course')
            course_name = input('课程名称(b退出)>>:').strip()
            if course_name == 'b':
                return
            if not Module.check_file('course',
                                     course_name) and len(course_name) != 0:
                course_period = input('周期(数字，单位month)>>:').strip()
                course_price = input('课程价格>>:').strip()
                course_time = input('上课时间>>:').strip()
                course_id = '%03d' % (len(course_list) + 1)       # 生成课程ID
                print(course_id)
                obj = Course(
                    course_name,
                    course_id,
                    course_period,
                    course_price,
                    course_time,
                    [],
                    '1',
                    [])  # 生成课程对象
                # 存储课程ID{ID:name}
                course_list[obj.course_id] = obj.course_name
                Module.save_file('course', obj.course_id, obj.structure)
                Module.save_file('course', 'course', course_list)
                return obj

            else:
                print('课程存在或者课程名不能为空！')

    @staticmethod
    def born_course(role, ID):
        '''
        从文件中获取内容实例化课程
        :param role:
        :param ID:
        :return:
        '''
        course_data = Module.get_data(role, ID)  # 从文件中读取课程信息
        course = Course(
            course_data['course_name'],
            course_data['course_id'],
            course_data['period'],
            course_data['perice'],
            course_data['course_time'],
            course_data['course_teacher'],
            course_data['state'])
        return course

    @staticmethod
    def update_course(role):
        '''
        更新课程信息：可进行课程上下架
        :param role:
        :return:
        '''
        while True:
            # 获取课程列表，massage结构为{ID:name}
            massage = Module.get_data(role, role)
            for k in massage.keys():
                course = Module.born_course(role, k)
                print(
                    course, '课程状态:%s' %
                    course.structure['state'])   # 打印所有课程的信息
            ID = input('输入修改课程ID(b退出)>>:').strip()
            if ID in massage.keys():
                change_obj = Module.born_course(
                    role, ID)                    # 实例化课程
                print(change_obj, '课程状态:%s' %
                      change_obj.structure['state'])  # 打印修改前的课程信息
                change_item = [
                    ['修改课程周期', 'period'],
                    ['修改课程价格', 'perice'],
                    ['修改上课时间', 'course_time'],
                    ['课程上下线', 'course_state']
                ]                                             # 可修改内容
                n = 0
                for i in change_item:
                    print(n, i[0])
                    n += 1
                choice = input('选择修改的选项序号(b,退出)>>:').strip()
                if choice.isdigit():
                    choice = int(choice)
                    if choice <= len(change_item):
                        if choice != 3:
                            change_data = input('输入修改后内容>>:').strip()
                            setattr(
                                change_obj,
                                change_item[choice][1],
                                change_data)  # 修改信息
                            new_msg = change_obj.course_structure(
                                change_obj.course_name,
                                change_obj.course_id,
                                change_obj.period,
                                change_obj.perice,
                                change_obj.course_time,
                                change_obj.course_teacher,
                                change_obj.course_state
                            )
                            Module.save_file(role, ID, new_msg)
                            Module.save_file(
                                role, ID, new_msg)        # 保存修改后的信息
                        elif choice == 3:                  # 课程下架后，将课程从开设的学校中移除
                            setattr(
                                change_obj, change_item[choice][1], change_data)
                            new_msg = change_obj.course_structure(
                                change_obj.course_name,
                                change_obj.course_id,
                                change_obj.period,
                                change_obj.perice,
                                change_obj.course_time,
                                change_obj.course_teacher,
                                change_obj.course_state
                            )
                            Module.save_file(role, ID, new_msg)
                            for i in change_obj.course_school:
                                school_massage = Module.get_data('school', i)
                                new_course_list = []
                                for j in school_massage['course_id']:
                                    if j != ID:
                                        new_course_list.append(j)
                                school_massage['course_id'] = new_course_list
                                Module.save_file('school', i, school_massage)
                                return change_obj['course_name']
                    else:
                        print('输入序号不合法!')
            elif ID == 'b':
                break

    @staticmethod
    def creat_teacher():
        '''
        创建老师对象
        :return:
        '''
        while True:
            teacher_name = input('老师姓名>>(b退出):').strip()
            if len(teacher_name) != 0:
                teacher_age = input('年龄>>:').strip()
                phone = input('电话>>:').strip()
                school = None
                password = Module.encrypt('123')
                teacher_course = None
                teacher_class = []
                student_id = []
                teacher_id = None
                obj = Teacher(
                    teacher_name, teacher_age, school, teacher_id,
                    teacher_course, phone, student_id, password, teacher_class
                )                                                 # 实例化老师对象
                return obj
            elif teacher_name == 'b':
                break

    @staticmethod
    def born_teacher(role, ID):
        '''
        从文件中读取信息实例化老师对象
        :param role:
        :param ID:
        :return:
        '''
        teacher_data = Module.get_data(role, ID)  # 从文件中读取课程信息
        teacher = Teacher(
            teacher_data['teacher_name'],
            teacher_data['teacher_age'],
            teacher_data['school'],
            teacher_data['teacher_id'],
            teacher_data['teacher_course'],
            teacher_data['phone'],
            teacher_data['student_id'],
            teacher_data['password'],
            teacher_data['teacher_class'])
        return teacher

    @staticmethod
    def update_teacher(role, ID):
        '''
        更新老师信息
        :param role:
        :return:
        '''

        while True:
            change_obj = Module.born_teacher(role, ID)   # 实例化老师
            print(change_obj)                           # 打印修改前的信息
            change_item = [['修改电话', 'phone'], ['姓名修改', 'teacher_name']]
            for index, i in enumerate(change_item):
                print(index, i[0])                       # 打印可修改的选项
            choice = input('选择修改的选项序号(b,退出)>>:').strip()
            if choice.isdigit():
                choice = int(choice)
                if choice <= len(change_item):
                    change_data = input('输入修改后内容>>:').strip()
                    setattr(
                        change_obj,
                        change_item[choice][1],
                        change_data)  # 修改信息
                    old_msg = Module.get_data(role, ID)
                    new_msg = change_obj.teacher_structure(
                        change_obj.teacher_name,
                        change_obj.teacher_age,
                        change_obj.phone,
                        change_obj.school,
                        change_obj.password,
                        change_obj.teacher_course,
                        change_obj.teacher_class,
                        change_obj.student_id,
                        change_obj.teacher_id
                    )
                    new_msg['state'] = old_msg['state']
                    Module.save_file(role, ID, new_msg)  # 保存修改后的信息
                else:
                    print('输入序号不合法!')
            elif choice == 'b':
                break
            else:
                print('查询不到该老师')

    @staticmethod
    def create_student():
        '''
        实例化学生
        :return:
        '''
        while True:
            student_name = input('姓名>>:').strip()
            if len(student_name) != 0:
                student_id = None
                age = input('年龄>>:').strip()
                phone = input('电话>>:').strip()
                student_school = None
                student_class = None
                c_password = input('设置密码>>:').strip()
                password = Module.encrypt(c_password)
                student_teacher = None
                obj = Student(
                    student_id, student_name, age, phone, student_school,
                    student_class, password, student_teacher, 0
                )
                return obj

    @staticmethod
    def born_student(role, ID):
        '''
        实例化学生对象
        :param role:
        :param ID:
        :return:
        '''
        student_data = Module.get_data(role, ID)  # 从文件中读取课程信息
        student = Student(
            student_data['id'],
            student_data['name'],
            student_data['age'],
            student_data['phone'],
            student_data['school'],
            student_data['class'],
            student_data['password'],
            student_data['teacher'],
            student_data['balance'])
        return student

    @staticmethod
    def update_student(role, ID):
        '''
        修改学生信息
        :param role:
        :param ID:
        :return:
        '''
        change_obj = Module.born_student(role, ID)  # 实例化学生
        print(change_obj)                           # 打印修改前的信息
        flag = True
        while flag:
            change_item = [['修改电话', 'phone'], ['姓名修改', 'name']]
            for index, i in enumerate(change_item):
                print(index, i[0])                  # 打印可修改的选项
            choice = input('选择修改的选项序号(b,退出)>>:').strip()
            if choice.isdigit():
                choice = int(choice)
                if choice <= len(change_item):
                    new_msg = Module.get_data(role, ID)
                    change_data = input('输入修改后内容>>:').strip()
                    new_msg[change_item[choice][1]] = change_data
                    Module.save_file(role, ID, new_msg)          # 保存修改后的信息
                else:
                    print('输入序号不合法!')
            elif choice == 'b':
                flag = False

    @staticmethod
    def creat_class():
        '''
        生成新的班级
        :return:
        '''
        class_list = Module.get_data('classes', 'classes')  # 数据结构{name:id}
        while True:
            class_name = input('班级名称(b退出)>>:').strip()
            if len(class_name) != 0 and class_name not in class_list.keys():
                class_id = '%03d' % (len(class_list) + 1)       # 生成班级ID
                class_students = []                              # 数据结构[id]
                school = None
                class_teacher = None
                class_volumetric = int(input('班级容量>>:').strip())
                classes = Class(
                    class_name,
                    class_id,
                    class_students,
                    school,
                    class_teacher,
                    class_volumetric)
                class_list[classes.class_id] = classes.class_name
                Module.save_file('classes', 'classes', class_list)
                Module.save_file(
                    'classes',
                    classes.class_id,
                    classes.structure)
                return classes
            else:
                print('班级名称不合法')

    @staticmethod
    def born_class(role, ID):
        '''
        通过文件生成班级
        :param role:
        :param ID:
        :return:
        '''
        class_data = Module.get_data(role, ID)  # 从文件中读取班级信息
        class_obj = Class(
            class_data['class_name'],
            class_data['class_id'],
            class_data['class_students'],
            class_data['school'],
            class_data['class_teacher'],
            class_data['class_volumetric'])
        return class_obj

    @staticmethod
    def select_school():
        '''
        选择学校
        :return:
        '''
        massage = Module.get_data('school', 'school')
        Module.show_school('school')
        while True:
            choice = input('输入学校ID>>:').strip()
            if choice in massage.keys():
                return choice
            else:
                print('学校ID不合法')
                continue

    @staticmethod
    def select_course(role, school_id):
        '''
        选择课程
        :param role:
        :param school_id:
        :return:
        '''

        if role == 'school':                              # 给学校绑定课程
            course_massage = Module.get_data('course', 'course')  # {ID:name}
            for k in course_massage.keys():
                print(Module.born_course('course', k))  # 打印课程信息
            course_ls = []
            while True:
                choice = input('选择课程编号(b退出)>>:').strip()
                if choice in course_massage.keys():
                    course_ls.append(choice)
                elif choice == 'b':
                    return course_ls
                else:
                    print('未开通课程')
                    continue
        else:                                            # 给老师和学生绑定课程
            while True:
                massage = Module.get_data('school', school_id)
                for i in massage['course_id']:
                    print(Module.born_course('course', i))  # 打印学校开设的课程
                choice = input('选择课程编号>>:').strip()
                if choice in massage['course_id']:
                    return choice
                else:
                    print('未开通的课程')
                    continue

    @staticmethod
    def select_teacher(course_id, school_id):
        '''
        选择老师
        :param course_id:
        :return:
        '''
        while True:
            massage = Module.get_data('course', course_id)
            for i in massage['course_teacher']:
                teacher_msg = Module.get_data('teacher', i)
                if school_id == teacher_msg['school']:         # 判断老师是不是在指定学校
                    teachers = Module.born_teacher('teacher', i)
                    print(teachers)                            # 打印该课程的代课老师信息
            choice = input('选择老师编号>>:').strip()
            if choice in massage['course_teacher']:
                return choice
            else:
                print('编号不合法')
                continue

    @staticmethod
    def select_class(teacher_id):
        '''
        选择班级
        :param teacher_id:
        :return:
        '''
        massage = Module.get_data('teacher', teacher_id)
        while True:
            for i in massage['teacher_class']:
                print(Module.born_class('classes', i))       # 打印该老师代课的所有班级
            choice = input('选择班级编号>>:').strip()
            if choice in massage['teacher_class']:
                class_obj = Module.born_class('classes', choice)
                if len(
                        class_obj.class_students) < int(
                        class_obj.class_volumetric):
                    return choice
                else:
                    print('已满员，请选择其他班级')
                    continue
            else:
                print('班级编号不合法')
                continue

    @staticmethod
    def show_student_score(student_id):
        '''
        学生课程成绩打印
        :param student_id:
        :return:
        '''
        massage = Module.get_data('student', student_id)
        course_name = Module.get_data(
            'course', massage['course'][0])['class_name']
        return '%s:%s' % (course_name, massage['course'][1])

    @staticmethod
    def del_massage(role, account_id):
        '''
        删除用户信息
        :param role:
        :param account_id:
        :return:
        '''
        path = r'%s\db\%s\%s.pkl'(setting.FILE_PATH, role, account_id)
        os.remove(path)

    @staticmethod
    def reset(role, account_id):
        '''
        用户状态重置，重置状态和密码
        :param role:
        :param account_id:
        :return:
        '''
        massage = Module.get_data(role, account_id)
        massage['state'] = 0                               # 重置用户状态
        massage['password'] = Module.encrypt('123')        # 重置用户密码，重置为123
        Module.save_file(role, account_id, massage)

    @staticmethod
    def change_password(role, account):
        '''
        修改密码
        :param role:
        :param account:
        :return:
        '''
        old_password = input('输入原来密码(b退出)>>:').strip()
        massage = Module.get_data(role, account)
        password = Module.encrypt(old_password)
        if old_password == 'b':
            return
        if password == massage['password']:
            new_password = input('输入新密码>>:').strip()
        if len(new_password) >= 6:
            massage['password'] = Module.encrypt(new_password)
            Module.save_file(role, account, massage)
        else:
            print('密码长度不够，必须6位以上!')
