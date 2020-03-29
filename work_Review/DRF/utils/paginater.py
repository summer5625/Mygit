# -*- coding: utf-8 -*-
# @Time    : 2020/2/24  20:43
# @Author  : XiaTian
# @File    : paginater.py
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class MyPagination(CursorPagination):

    page_size = 2  # 每页显示多少数据
    cursor_query_param = 'cursor'  # url上游标的键值
    ordering = '-id'  # 排序规则


    