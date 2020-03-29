# -*- coding: utf-8 -*-
# @Time    : 2019/10/19  13:42
# @Author  : XiaTian
# @File    : my_tags.py


from django import template
from django.db.models import Count
from django.db.models.functions import TruncMonth # 导入日期归档函数

from blog.models import *

register = template.Library()


@register.inclusion_tag('classification_tag.html') # 要有一个参数，参数是要渲染的标签模板
def classification_tag(username):
    '''
    自定义侧边栏标签
    :param username:
    :return:
    '''

    ret = UserInfo.objects.filter(username=username).first()

    blog = ret.blog

    category_list = Category.objects.filter(blog=blog).values('pk').annotate(c=Count('article__pk')).values_list(
        'title', 'c')

    tag_list = Tag.objects.filter(blog=blog).values('pk').annotate(c=Count('article__aid')).values_list('title', 'c')

    date_list = Article.objects.filter(user=ret).annotate(month=TruncMonth('create_time')).values('month').annotate(
        c=Count('pk')).values_list('month', 'c')

    return {'ret': ret, 'blog': blog, 'category_list': category_list, 'tag_list': tag_list, 'date_list': date_list}