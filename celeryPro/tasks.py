# -*- coding: utf-8 -*-
# @Time    : 2020/3/23  14:47
# @Author  : XiaTian
# @File    : tasks.py
from __future__ import absolute_import
from celeryPro.celery import app


@app.task
def add(x, y):
    return x + y

