# -*- coding: utf-8 -*-
# @Time    : 2020/2/12  22:02
# @Author  : XiaTian
# @File    : school.py
from stark.service.handle_table import Handler
from .base import PermissionHandler


class SchoolHandler(PermissionHandler, Handler):
    
    has_add_btn = True
    list_display = ['title', Handler.display_edit, Handler.display_del]
