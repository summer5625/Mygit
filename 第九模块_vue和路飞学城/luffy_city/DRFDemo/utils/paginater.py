# -*- coding: utf-8 -*-
# @Time    : 2019/11/27  16:53
# @Author  : XiaTian
# @File    : paginater.py
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


# 继承PageNumberPagination的分页器
# class MyPagination(PageNumberPagination):
#     page_size = 2
#     page_query_param = 'page'
#     page_size_query_param = 'size'
#     max_page_size = 3


# 继承LimitOffsetPagination的分页器，LimitOffsetPagination是从第几条开始找，向后找多少条
# class MyPagination(LimitOffsetPagination):
#     default_limit = 1 # 向后找一条
#     limit_query_param = 'limit'  # 向后找多少条， url上参数的关键字
#     offset_query_param = 'offset'  # 从你第几条开始找， url上参数的关键字
#     max_limit = 3 # 最大限制


# 继承CursorPagination的分页器，游标分页，可以对数据排序，对游标加密
class MyPagination(CursorPagination):
    page_size = 2 # 每页显示多少条
    cursor_query_param = 'cursor'
    ordering = '-id'  # 排序规则