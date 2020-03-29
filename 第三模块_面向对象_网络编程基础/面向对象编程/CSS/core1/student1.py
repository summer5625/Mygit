# -*- coding: utf-8 -*-
# @Time    : 2019/4/7 12:27
# @Author  : XiaTian
# @File    : student1.py

import os
import sys
import pickle

class Modules:

    def show_all_course(self):
        with open('course_info', 'rb') as f:
            count = 1
            while True:
                try:
                    course_obj = pickle.load(f)
                    print(count, course_obj.name, course_obj.price, course_obj.period, course_obj.teacher)
                    count += 1
                except EOFError:
                    break

class Course:

    def __init__(self,name,price,period,teacher):

        self.name = name
        self.price = price
        self.period = period
        self.teacher = teacher

class Student(Modules):

    function_list = [
                        ('查看课程', 'show_all_course'),
                        ('选择课程', 'select_course'),
                        ('查看已选课程', 'check_course'),
                        ('退出', 'exit')
                    ]
    def __init__(self,name):

        self.name = name
        self.course = []

    def select_course(self):
        self.show_all_course()
        number = int(input('序号>>:').strip())
        count = 1
        with open('course_info','rb') as f:
            while True:
                try:
                    course_obj = pickle.load(f)
                    if number == count:
                        self.course.append(course_obj)
                        print('%s课程选择成功!'%course_obj.name)
                        break
                    count += 1
                except EOFError:
                    print('无该课程')
                    break

    def check_course(self):

        for i in self.course:
            print(i.name,i.teacher)

    @staticmethod
    def init(name):
        '''
        返回一个学生对象，找到符合的对象后返回该对象
        :param name:
        :return:
        '''
        with open('student_info','rb') as f:
            while True:
                try:
                    student_obj = pickle.load(f)
                    if student_obj.name == name:
                        return  student_obj
                except EOFError:
                    print('没有这个学生')
                    break

    def exit(self):
        with open('student_info','rb') as f1,open('student_info_new','wb') as f2:
            while True:
                try:
                    student_obj = pickle.load(f1)
                    if student_obj.name == self.name:
                        pickle.dump(self,f2)
                    else:
                        pickle.dump(student_obj,f2)
                except EOFError:
                    break
        os.remove('student_info')
        os.rename('student_info_new','student_info')
        exit()

class Manager(Modules):

    function_list = [
                        ('创建课程','creat_course'),
                        ('创建学生','creat_student'),
                        ('查看所有课程','show_all_course'),
                        ('查看所有学生选课','show_student_course'),
                        ('查看所有学生','show_all_student'),
                        ('退出','exit')
                    ]

    def __init__(self,name):

        self.name = name

    def creat_course(self):
        name = input('course_name>>:').strip()
        price = input('course_price>>:').strip()
        period = input('course_period>>:').strip()
        teacher = input('course_teacher>>:').strip()
        course_obj = Course(name,price,period,teacher)
        with open('course_info','ab') as f:
            pickle.dump(course_obj,f)
        print('%s课程创建'%name)

    def creat_student(self):
        name = input('student_name>>:').strip()
        password = input('student_password>>:').strip()
        student_obj = Student(name)
        student_info = '%s/%s/Student\n'%(name,password)
        with open('userinfo.txt','a') as f:
            f.write(student_info)

        with open('student_info','ab') as f1:
            pickle.dump(student_obj,f1)
        print('%s学生创建成'%name)

    def show_all_student(self):
        with open('student_info', 'rb') as f:
            count = 1
            while True:
                try:
                    student_obj = pickle.load(f)
                    print(count, student_obj.name)
                    count += 1
                except EOFError:
                    break

    def show_student_course(self):
        with open('student_info','rb') as f:
            while True:
                try:
                    student_obj = pickle.load(f)
                    course_name = [i.name for i in student_obj.course]
                    print(student_obj.name,'所选课程%s'%'|'.join(course_name))
                except EOFError:
                    break


    @classmethod
    def init(cls,name):
        '''
        返回一个管理员对象
        :param name:
        :return:
        '''
        return cls(name)

    def exit(self):
        exit()



def landing():

    name = input('name>>:').strip()
    pawd = input('password>>:').strip()
    with open('userinfo.txt',encoding='utf-8') as f:
        for line in f:
            user,pwd,identify = line.strip().split('/')
            if name == user and pawd == pwd:
                return {'result':True,'name':user,'id':identify}
        else:
            return {'result':False,'name':user}

ret = landing()
if ret['result']:
    print('\033[2;32;40m登录成功!\033[0m')
    if hasattr(sys.modules[__name__],ret['id']):           # 判断从文件里面读取内容在没在
        cls = getattr(sys.modules[__name__],ret['id'])     # 用读取的内容进行类的实例化
        obj = cls.init(ret['name'])                        # 实例化对象
    while True:
        for id,item in enumerate(cls.function_list,1):
            print(id,item[0])
        func_str =  cls.function_list[int(input('>>:'))-1][1]
        if hasattr(obj,func_str):
            getattr(obj,func_str)()

