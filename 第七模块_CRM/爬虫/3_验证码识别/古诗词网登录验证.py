# -*- coding: utf-8 -*-
# @Time    : 2019/12/4  22:32
# @Author  : XiaTian
# @File    : 古诗词网登录验证.py
import requests
from lxml import etree
import os
import sys

DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(DIR)

from codeClass import YDMHttp


def getCode(file, codeType):
    # 用户名
    username = 'summer5625'

    # 密码
    password = 'xiayun519625'

    # 软件ＩＤ，开发者分成必要参数。登录开发者后台【我的软件】获得！
    appid = 1

    # 软件密钥，开发者分成必要参数。登录开发者后台【我的软件】获得！
    appkey = '1f4b564483ae5c907a1d34f8e2f2776c'

    # 图片文件
    filename = file

    # 验证码类型，# 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。在此查询所有类型 http://www.yundama.com/price.html
    codetype = codeType

    # 超时时间，秒
    timeout = 60
    result = None
    # 检查
    if (username == 'username'):
        print('请设置好相关参数再测试')
    else:
        # 初始化
        yundama = YDMHttp(username, password, appid, appkey)

        # 登陆云打码
        uid = yundama.login()
        print('uid: %s' % uid)

        # 查询余额
        balance = yundama.balance()
        print('balance: %s' % balance)

        # 开始识别，图片路径，验证码类型ID，超时时间（秒），识别结果
        cid, result = yundama.decode(filename, codetype, timeout)
        print('cid: %s, result: %s' % (cid, result))

    return result


if __name__ == '__main__':
    url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }

    pag_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(pag_text)
    code_img_src = 'https://so.gushiwen.org' + tree.xpath('//img[@id="imgCode"]/@src')[0]

    with open('code.jpg', 'wb') as f:

        photo = requests.get(url=code_img_src, headers=headers).content
        f.write(photo)

    result = getCode('code.jpg', 1004)
    print(result)


