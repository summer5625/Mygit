# -*- coding: utf-8 -*-
# @Time    : 2019/11/13  22:27
# @Author  : XiaTian
# @File    : base.py

from django.conf import settings
from stark.service.handle_table import Handler


class PermissionHandler(Handler):

    def get_add_btn(self, request, *args, **kwargs):
        '''
        判断当前用户是否有添加按钮权限
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''

        # 当前用户权限信息
        permission_dict = request.session.get(settings.PERMISSION_KEY)

        if self.get_add_url_name not in permission_dict:

            return None
        return super().get_add_btn(request, *args, **kwargs)

    def get_list_display(self, request, *args, **kwargs):
        '''
        判断当前用户是否有编辑和删除权限
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''

        permission_dict = request.session.get(settings.PERMISSION_KEY)
        value = []

        if self.list_display:
            value.extend(self.list_display)

            if self.get_del_url_name not in permission_dict and type(self).display_del in value:

                value.remove(type(self).display_del)

            elif self.get_edit_url_name not in permission_dict and type(self).display_edit in value:

                value.remove(type(self).display_edit)

        return value




