# -*- coding: utf-8 -*-
# @Time    : 2019/10/16  23:04
# @Author  : XiaTian
# @File    : valid_img.py

import random
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO #引入内存管理工具，使生成的随机验证码图片加载到内存中，提高速度


def random_color():
    '''
    生成图片随机背景色
    :return:
    '''
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


#随机验证码字符
def random_char():

    random_num = str(random.randint(0, 9))
    random_low_alpha = chr(random.randint(97, 122))
    random_up_aloha = chr(random.randint(65, 90))
    random_character = random.choice([random_num, random_low_alpha, random_up_aloha])

    return random_character


def new_valid_img(request):
    # 方式一提交图片
    # with open('表关系图.jpg', 'rb') as f:
    #
    #     data = f.read()

    # 方拾贰
    # 生成新图片
    # mage.new(mode, size,
    # color),参数有三个：图片的格式一般RGB，size图片的大小，用元组表示图片的宽高；color图片的背景色
    # img = Image.new('RGB', (170, 50), color=random_color())

    # 保存新生成的图片
    # with open('validCode.png', 'wb') as f:

    # img.save(f, 'png')

    # 读取图片
    # with open('validCode.png', 'rb') as f:

    # data = f.read()

    # 方式三

    img = Image.new('RGB', (170, 50), color=random_color())

    # 在生成图片上写字
    draw = ImageDraw.Draw(img)

    # 添加文字的字体样式，truetype(font, size=10),两个参数：font是字体样式，size是字体大小，默认10px
    font = ImageFont.truetype('static/blog/fronts/Teen_Light_Italic.ttf', size=30)

    # 在图片上提添加文字，text((x,y), text,font_color, font),(x,y)是文字在画板的位置(即图片中的位置)，text是文字内容，
    # font_color文字颜色，font字体样式

    valid_code = ''
    for i in range(5):
        new_str = random_char()
        draw.text((i * 30 + 20, 5), new_str, random_color(), font=font)

        valid_code += new_str

    request.session['valid_code_str'] = valid_code  # 保存刷新的验证码到session

    # width = 170
    # height = 50

    # 生成噪线
    # for i in range(10):
    #     x1 = random.randint(0,width)
    #     x2 = random.randint(0, width)
    #     y1 = random.randint(0,height)
    #     y2 = random.randint(0,height)
    #     draw.line((x1, y1, x2, y2), fill=random_color())
    # 生成噪点
    # for i in range(100):
    #     draw.point([random.randint(0, width), random.randint(0, height)], fill=random_color())
    #     x = random.randint(0, width)
    #     y = random.randint(0, height)
    #     draw.arc((x, y, x+4, y+4), 0, 90, fill=random_color())

    f = BytesIO()  # 存图片
    img.save(f, 'png')
    data = f.getvalue()  # 取图片

    return data
