# -*- coding: utf-8 -*-
# @Time    : 2020/3/23  14:46
# @Author  : XiaTian
# @File    : celery.py
from __future__ import absolute_import
from celery import Celery


app = Celery('celeryPro', include=['celeryPro.tasks'])

app.config_from_object('celeryPro.config')


if __name__ == '__main__':
    app.start()