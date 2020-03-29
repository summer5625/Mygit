# -*- coding: utf-8 -*-
# @Time    : 2020/3/23  14:28
# @Author  : XiaTian
# @File    : mycelery.py
from celery import  Celery


brokers = 'redis://127.0.0.1:6379/5'
backend = 'redis://127.0.0.1:6379/6'

app = Celery('tasks', broker=brokers, backend=backend)


@app.task
def add(x, y):
    return x + y