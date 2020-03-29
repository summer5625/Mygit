# -*- coding: utf-8 -*-
# @Time    : 2019/12/29  1:27
# @Author  : XiaTian
# @File    : logger.py
import logging.handlers
import logging
import time
import os


class Logger(object):

    def __init__(self, logger):

        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        rq = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        log_path = base_path + '/log/'
        log_name = log_path + rq + '.log'
        # fh = logging.handlers.RotatingFileHandler(log_name, maxBytes=1024*1024, backupCount=5, encoding='utf-8')
        fh = logging.FileHandler(log_name, encoding='utf-8')
        fh.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)




    def getlog(self):

        return self.logger


