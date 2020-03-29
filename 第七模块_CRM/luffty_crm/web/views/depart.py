# -*- coding: utf-8 -*-
# @Time    : 2019/11/9  15:19
# @Author  : XiaTian
# @File    : depart.py

from stark.service.handle_table import Handler
from .base import PermissionHandler


class DepartmentHandler(PermissionHandler, Handler):
    has_add_btn = True

    list_display = ['title', Handler.display_edit, Handler.display_del]