# -*- coding: utf-8 -*-
# @Time    : 2019/11/3  20:01
# @Author  : XiaTian
# @File    : stark.py

from django.urls import path, re_path, reverse
from django.shortcuts import HttpResponse
from django.utils.safestring import mark_safe
from django import forms

from app01.models import *
from stark.service.handle_table import site, Handler, get_choice_text, StarkModelForm, SearchOption


class HandelDepartment(Handler):
    list_display = ['title', Handler.display_edit, Handler.display_del]
    has_add_btn = True

    # def get_urls(self):
    #     patterns = [
    #         path('list/', self.list_view),
    #         path('add/', self.add_view),
    #         re_path(r'detail/(\d+)/$', self.detail_view)
    #     ]
    #
    #     patterns.extend(self.extra_urls())
    #
    #     return patterns

    def detail_view(self):
        return HttpResponse('详细页面')


class UserInfoModelForm(StarkModelForm):
    """
    自定义form组件
    """

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

    search_list = ['name__contains', 'email__contains']  # 定义模糊查询的查询条件

    action_list = [Handler.multi_delete, ]

    search_group = [SearchOption('gender', text_func=lambda field_obj: field_obj[1]+'333'), # 定制筛选按钮显示文字
                    SearchOption('depart', {'id__gt': 0}, is_multi=True)]

    def display_depart(self, obj=None, is_header=None):
        '''
        定义页面显示信息，当需要进行连表查询时用，如果表的类设置了__str__方法可以直接显示，没有定义此方法可以用这个
        :param obj:
        :param is_header:
        :return:
        '''
        if is_header:
            return '部门'
        return obj.depart.title

    # def save(self, form, is_update=False):
    #     form.instance.depart_id = 1
    #     form.save()

    # 定制页面显示列
    list_display = [Handler.display_checkbox, 'name', get_choice_text('性别', 'gender'), 'email', display_depart,
                    Handler.display_edit, Handler.display_del]


site.register(Department, HandelDepartment)
site.register(UserInfo, HandelUserInfo)
