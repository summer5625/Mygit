# -*- coding: utf-8 -*-
# @Time    : 2020/3/23  14:47
# @Author  : XiaTian
# @File    : config.py
from __future__ import absolute_import


CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/5'
BROKEN_URL = 'redis://127.0.0.1:6379/6'