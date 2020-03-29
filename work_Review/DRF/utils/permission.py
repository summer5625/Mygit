# -*- coding: utf-8 -*-
# @Time    : 2020/2/24  15:34
# @Author  : XiaTian
# @File    : permission.py
from rest_framework.permissions import BasePermission



class MyPermission(BasePermission):

    message = '您还不是VIP，没有访问权限'

    def has_permission(self, request, view):

        user_obj = request.user
        
        if int(user_obj.type) == 3:
            return False
        return True

