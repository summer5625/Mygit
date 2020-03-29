# -*- coding: utf-8 -*-
# @Time    : 2019/9/17  22:02
# @Author  : XiaTian
# @File    : server.py

import json

from flask import Flask
from flask import request
from flask import Response

app = Flask(__name__)

#默认请求模式是get
@app.route('/')
def index():
    resp = Response('<h2>首页</h2>')
    resp.headers['Access-Control-Allow-Origin'] = '*'

    return resp


@app.route('/course')
def course():
    resp = Response(json.dumps({
        'name':'张三'
    }))

    resp.headers['Access-Control-Allow-Origin'] = '*'

    return resp


@app.route('/create', methods=['post', ])
def create():
    print(request.form.get('name'))

    with open('user.json', 'r', encoding='utf-8') as f:
        data = json.loads(f.read())

    data.append({"name":request.form.get('name')})

    with open('user.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(data))

    resp = Response(json.dumps(data))

    resp.headers['Access-Control-Allow-Origin'] = '*'

    return resp


if __name__ == '__main__':
    app.run(host='localhost', port=8800)