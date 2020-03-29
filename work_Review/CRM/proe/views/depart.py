# -*- coding: utf-8 -*-
# @Time    : 2020/2/12  22:45
# @Author  : XiaTian
# @File    : depart.py
from stark.service.handle_table import Handler
from .base import PermissionHandler


class DepartHandler(PermissionHandler, Handler):
    
    has_add_btn = True
    list_display = ['title', Handler.display_edit, Handler.display_del]