# -*- coding: utf-8 -*-
# @Time    : 2019/12/4  16:54
# @Author  : XiaTian
# @File    : 5_xpath解析.py

from lxml import etree


if __name__ == '__main__':

    # 将本地的HTML文件加载到etree中
    tree = etree.parse('text.html')

    # 使用xpath表达式获取文件中的标签和属性
    # r = tree.xpath('/html/body/div')  # / 表示从根节点开始定位，只能一级一级向下找，不能跳级。表示一个层级
    # r = tree.xpath('/html//div')  # // 表示多个层级。
    # r = tree.xpath('//div')  # // 也可表示可以从任意位置查找标签
    # r = tree.xpath('//div[@class="song"]')  # 利用标签的属性进行标签定位查找
    # r = tree.xpath('//div[@class="song"]/p[1]') # 利用索引值进行精确定位标签，索引从1开始
    # r = tree.xpath('//div[@class="tang"]//text()') # 获取标签中的文本内容//获取当前标签下包括子标签的所有文本
    r = tree.xpath('//div[@class="song"]/img/@src')[0] # 获取标签中的属性值


    print(r)
