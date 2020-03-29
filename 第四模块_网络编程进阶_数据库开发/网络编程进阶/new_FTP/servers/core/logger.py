# -*- coding: utf-8 -*-
# @Time    : 2019/4/17 22:51
# @Author  : XiaTian
# @File    : logger.py

import logging

from conf import setting


class Logger:

    @staticmethod
    def logs(log_type):

        logger = logging.getLogger(log_type)
        logger.handlers.clear()                                     # 用户日志输出优化，去除重复日志
        logger.setLevel(setting.LOG_LEVEL)
        logger_path = r'%s\log\%s' % (
            setting.BASIS_DIR, setting.LOG_TYPE[log_type])
        fh = logging.FileHandler(logger_path, encoding=setting.CODING)
        logger.addHandler(fh)
        log_formatter = logging.Formatter(
            '%(asctime)s  %(levelname)s  %(message)s',
            datefmt='%Y-%m-%d %I:%M:%S %p')
        fh.setFormatter(log_formatter)

        return logger
