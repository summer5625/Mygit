# -*- coding: utf-8 -*-
# @Time    : 2019/11/9  15:20
# @Author  : XiaTian
# @File    : course.py

from stark.service.handle_table import Handler
from .base import PermissionHandler


class CourseHandler(PermissionHandler, Handler):

    has_add_btn = True

    list_display = ['title', Handler.display_edit, Handler.display_del]