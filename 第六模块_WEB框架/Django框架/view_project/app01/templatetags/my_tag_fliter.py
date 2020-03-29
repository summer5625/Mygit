# -*- coding: utf-8 -*-
# @Time    : 2019/9/27  15:10
# @Author  : XiaTian
# @File    : my_tag_fliter.py

from django import template


register = template.Library() #变量名称必须为register


#自定义过滤器,只能传两个参数
@register.filter
def multi_fliter(x,y):

    return x*y


#自定义标签
@register.simple_tag
def multi_tag(x,y):

    return x*y