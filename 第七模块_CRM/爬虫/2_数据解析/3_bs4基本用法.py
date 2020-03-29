# -*- coding: utf-8 -*-
# @Time    : 2019/12/4  15:04
# @Author  : XiaTian
# @File    : 3_bs4基本用法.py
from bs4 import BeautifulSoup


if __name__ == '__main__':

    # 实例化BeautifulSoup对象
    fp = open('text.html', 'r', encoding='utf-8')

    # 实例化时有两个参数：第一个参数是要解析的内容，第二个是解析文本内容的组件
    # 解析的内容可以使本地的一个文件，也可以是爬取的页面内容
    soup = BeautifulSoup(fp, 'lxml')

    # ########################基本用法# ########################

    # 1、获取标签方法,格式：soup.标签名称
    # 这种方法只能获取第一个标签
    # print(soup.a)
    # print(soup.div)
    # print(soup.find("a")) # 获取的是符合条件的第一个标签
    # print(soup.find('div', class_='song')) # 获取指定属性的标签
    # print(soup.find('a', id='feng'))
    # print(soup.find_all('a'))  # 找到所有指定标签
    # print(soup.find_all(['a', 'li']))
    # print(soup.find_all(['a', 'li'], limit=2)) # 找前两个标签

    # 2、获取属性
    # print(soup.a.attrs) # 也只能获取第一个标签内的所有属性和值，返回字典
    # print(soup.a.attrs['href']) # 获取指定的属性值
    # print(soup.a['href']) # 获取指定的属性值

    # 3、获取标签内的文本内容
    # print(soup.a.string) # 只获取标签下的文本内容，不获取其子标签中的文本内容
    # print(soup.find('div', class_='song').text) # 获取标签下所有的文本内容，子标签的也获取
    # print(soup.find('div', class_='song').get_text()) # 获取标签下所有的文本内容，子标签的也获取

    # 4、select方法

    # 标签选择器，返回列表
    # print(soup.select('li'))
    # print(soup.select('.song'))
    # print(soup.select('#feng'))

    # 子代选择器
    # print(soup.select('div > ul > li > .du')) # >只能选择中定标签的直系子代
    print(soup.select('div ul li a')) # 选择所有的子代































