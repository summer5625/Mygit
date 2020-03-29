# -*- coding: utf-8 -*-
# @Time    : 2019/12/5  22:36
# @Author  : XiaTian
# @File    : flask服务器.py
from flask import Flask
import time


app = Flask(__name__)


@app.route('/summer')
def index_summer():
    time.sleep(2)
    return 'Hello summer'


@app.route('/jay')
def index_jay():
    time.sleep(2)
    return 'Hello jay'


@app.route('/tom')
def index_tom():
    time.sleep(2)
    return 'Hello tom'


if __name__ == '__main__':
    app.run(threaded=True)