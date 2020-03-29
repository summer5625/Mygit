# -*- coding: utf-8 -*-
# @Time    : 2019/12/5  13:49
# @Author  : XiaTian
# @File    : 7_模拟人人网登陆.py
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
    appid = 6003

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

    url = 'http://www.renren.com/SysHome.do'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }

    login_pag = requests.get(url=url, headers=headers).text

    login_tree = etree.HTML(login_pag)

    code_img_src = login_tree.xpath('//img[@id="verifyPic_login"]/@src')[0]

    code_content = requests.get(url=code_img_src, headers=headers).content

    with open('code.jpg', 'wb') as f:
        f.write(code_content)

    code = getCode('code.jpg', 5000)

    # post请求，验证登陆
    login_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019114140808'

    data = {
        'email': '17634407602',
        'icode': code,
        'origURL': 'http://www.renren.com/home',
        'domain': 'renren.com',
        'key_id': '1',
        'captcha_type': 'web_login',
        'password': '1d6806748d88f2d4c7277ca0828860128369249f21df6aa8861b1e0fa94c07bd',
        'rkey': '83f9b743701ba5215116e01c41cec09a',
        'f': 'http%3A%2F%2Fwww.renren.com%2F973019309%2Fnewsfeed%2Fphoto',
    }

    response = requests.post(url=login_url, headers=headers, data=data)

    # 获取响应状态码，看是否登录成功
    print(response.status_code)
    land_pag = response.text

    with open('login.html', 'w', encoding='utf-8') as f:

        f.write(land_pag)























