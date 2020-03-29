# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 0:43
# @Author  : XiaTian
# @File    : logger.py

import logging

from conf import setting


class Logger:

    @staticmethod
    def logs(role):
        '''
        生成用户操作日志
        :param role: 用户角色：管理员、老师、学生
        :return:
        '''
        logger = logging.getLogger(role)
        logger.handlers.clear()  # 用户日志输出优化，去除重复日志
        logger.setLevel(setting.LOG_LEVEL)
        logger_path = r'%s\log\%s' % (setting.FILE_PATH, setting.LOG_TYPE[role])
        fh = logging.FileHandler(logger_path, encoding='utf-8')
        logger.addHandler(fh)
        log_formatter = logging.Formatter('%(asctime)s  %(levelname)s  %(message)s',
                                          datefmt='%Y-%m-%d %I:%M:%S %p'
                                          )
        fh.setFormatter(log_formatter)

        return logger