# -*- coding: utf-8 -*-
# @Time    : 2019/11/27  13:56
# @Author  : XiaTian
# @File    : permission.py
from rest_framework.permissions import BasePermission


class MyPermission(BasePermission):
    message = '您还不是VIP，没有访问权限，滚吧'

    def has_permission(self, request, view ):
        # 判断用户是否有权限
        user_obj = request.user
        if user_obj.type == 3:
            return False
        else:
            return True
    