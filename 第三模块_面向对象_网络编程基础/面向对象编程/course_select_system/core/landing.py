# -*- coding: utf-8 -*-
# @Time    : 2019/3/27 22:40
# @Author  : XiaTian
# @File    : landing.py

from core.modules import Module
from core.logger import Logger


def manager_landing(func):
    '''
    管理员登录装饰器
    :param func:
    :return:
    '''
    def inner():
        count = 0
        while count < 3:
            account = input('请输入管理员账号(b退出程序)>>:').strip()
            if account == 'b':
                return
            password = input('请输入密码>>:').strip()
            if account == 'admin' and password == 'admin':
                print('登录成功!')
                log_massage = 'role:manager   account:admin   operation:landing   info:管理员成功登录!'  # 日志信息
                loggers = Logger.logs('manager')
                # 记录日志
                loggers.info(log_massage)
                return func()
            else:
                print('账号或密码错误!')
                count += 1

        if count == 3:
            print('当日密码输入次数过多!')
            error = 'role:admin   account:admin   operation:landing   info:密码输入次数过多!'
            loggers = Logger.logs('manager')
            # 记录错误日志
            loggers.error(error)
    return inner


def landing(role):
    '''
    老师和学生认证装饰器
    :param func:
    :return:
    '''
    n = 0
    while True:
        account = input('输入账号>>:').strip()
        file_path = Module.check_file(role, account)
        if file_path:                                    # 账号校验
            massage = Module.get_data(role, account)
        else:
            print('用户未注册!')
            continue
        if massage['state'] == 0:                         # 检查用户状态
            r_password = input('输入密码>>:').strip()
            password = Module.encrypt(r_password)
        else:
            print('账号被冻结，请联系管理员解除锁定!')
            exit()                                        # 账号冻结退出程序
        if password == massage['password']:               # 密码校验
            print('登录成功!')
            landing_log = 'role:%s   account:%s   operation:landing   info:登录成功!' % (
                role, account)
            loggers = Logger.logs(role)
            loggers.info(landing_log)
            return account
        else:
            print('密码错误，请重新输入!')
            n += 1
        if n >= 3:
            print('密码输入错误次数过多，账号被冻结!')
            massage['state'] = 1
            Module.save_file(role, account, massage)
            landing_error = 'role:%s   account:%s   operation:landing   info:账号被冻结!' % (
                role, account)
            loggers = Logger.logs(role)
            loggers.error(landing_error)
            return
