# -*- coding: utf-8 -*-
# @Time    : 2020/2/11  13:22
# @Author  : XiaTian
# @File    : stark.py
from django.shortcuts import HttpResponse
from web1.models import *
from skk.service.handle_table import site, Handler, get_choice_text, StarkModelForm, SearchOption


class HandelDepartment(Handler):

    list_display = ['title', Handler.display_edit, Handler.display_del]
    has_add_btn = True

    def detail_view(self):
        return HttpResponse('详细页面')


class UserInfoModelForm(StarkModelForm):

    class Meta:
        model = UserInfo
        fields = ['name', 'gender', 'password', 'email', 'depart']


class MyOption(SearchOption):

    def get_db_condition(self, request, *args, **kwargs):
        return


class HandelUserInfo(Handler):

    has_add_btn = True
    per_page_count = 3
    model_form_class = UserInfoModelForm
    search_list = ['name__contains', 'email__contains']
    action_list = [Handler.multi_delete, ]
    search_group = [SearchOption('gender', text_func=lambda field_obj: field_obj[1] + '333'),
                    SearchOption('depart', {'id__gt': 0}, is_multi=True)]

    def display_depart(self, obj=None, is_header=None):

        if is_header:
            return '部门'
        return obj.depart.title

    list_display =[Handler.display_checkbox, 'name', get_choice_text('性别', 'gender'), 'email', display_depart,
                   Handler.display_edit, Handler.display_del]


class HandelHost(Handler):
    has_add_btn = True


class HandelRole(Handler):
    has_add_btn = True


site.register(UserInfo, HandelUserInfo)
site.register(Department, HandelDepartment)
site.register(Host, HandelHost)
site.register(Role,HandelRole)




























