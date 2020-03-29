# -*- coding: utf-8 -*-
# @Time    : 2020/2/12  22:48
# @Author  : XiaTian
# @File    : course.py
from stark.service.handle_table import Handler
from .base import PermissionHandler


class CourseHandler(PermissionHandler, Handler):

    has_add_btn = True
    list_display = ['title', Handler.display_edit, Handler.display_del]