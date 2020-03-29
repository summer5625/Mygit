# -*- coding: utf-8 -*-
# @Time    : 2019/12/4  11:21
# @Author  : XiaTian
# @File    : 1_正则之糗百图片爬取.py

import requests


if __name__ == '__main__':

    url = 'https://image.hahamx.cn/2019/12/04/middle/2912234_a46437e547f6083fef909460deec2ddb_1575429582.gif'
    'https://image.hahamx.cn/2019/12/04/normal/2912165_dcd9713f02aefe46e30a8b5795fcfaff_1575389821.gif'

    # content获取的是二进制的数据
    photo = requests.get(url=url).content

    with open('photo.gif', 'wb') as f:
        f.write(photo)