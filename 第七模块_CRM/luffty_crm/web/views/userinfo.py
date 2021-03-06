# -*- coding: utf-8 -*-
# @Time    : 2019/11/9  15:19
# @Author  : XiaTian
# @File    : userinfo.py

from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from django.urls import re_path
from django.shortcuts import HttpResponse, render, redirect

from web import models
from stark.service.handle_table import Handler, StarkModelForm, get_choice_text, SearchOption
from web.utils.md5 import get_md5
from .base import PermissionHandler


class UserInfoAddModelForm(StarkModelForm):
    confirm_password = forms.CharField(label='确认密码')  # 给表单新增字段

    class Meta:
        model = models.UserInfo
        fields = ['name', 'nickname', 'gender', 'phone', 'email', 'password', 'confirm_password', 'depart', 'roles']

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if password != confirm_password:
            raise ValidationError('两次密码不一致')
        return confirm_password

    def clean(self):
        '''
        将设置的密码加密后存到数据库
        :return:
        '''
        password = self.cleaned_data['password']
        self.cleaned_data['password'] = get_md5(password)

        return self.cleaned_data


class UserInfoChangeModelForm(StarkModelForm):
    class Meta:
        model = models.UserInfo
        fields = ['name', 'nickname', 'gender', 'phone', 'email', 'depart', 'roles']


class UserInfoPasswordModelForm(forms.Form):

    password = forms.CharField(label='密码', widget=widgets.PasswordInput(attrs={'class': "form-control"}))
    confirm_password = forms.CharField(label='确认密码', widget=widgets.PasswordInput(attrs={'class': "form-control"}))

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if password != confirm_password:
            raise ValidationError('两次密码不一致')
        return confirm_password


class UserInfoHandler(PermissionHandler, Handler):

    has_add_btn = True

    search_group = [SearchOption('gender'), SearchOption('depart', is_multi=True)]

    search_list = ['name__contains', 'nickname__contains', 'depart__title__contains']

    def get_model_form_class(self, is_add, request, pk, *args, **kwargs):
        '''
        根据编辑和添加表单不同，提供不同的modelform
        :param is_add:
        :return:
        '''

        if is_add:
            return UserInfoAddModelForm
        return UserInfoChangeModelForm

    def display_reset_password(self, obj=None, is_header=None, *args, **kwargs):

        if is_header:
            return '重置密码'

        return mark_safe("<a href='%s'>重置密码</a>" % self.reverse_reset_password_url(pk=obj.pk))

    @property
    def get_reset_password_url_name(self):

        return self.get_url_name('reset_password')

    def reverse_reset_password_url(self, *args, **kwargs):

        return self.reverse_common_url(self.get_reset_password_url_name, *args, **kwargs)

    def extra_urls(self):

        patterns = [re_path(r'^reset/password/(?P<pk>\d+)/$', self.wrapper(self.reset_password_view),
                            name=self.get_reset_password_url_name)]
        return patterns

    def reset_password_view(self, request, pk, *args, **kwargs):

        user_obj = models.UserInfo.objects.filter(pk=pk).first()
        if not user_obj:
            return HttpResponse('用户不存在!')

        if request.method == 'GET':
            form = UserInfoPasswordModelForm()

            return render(request, 'stark/change.html', {'form': form})
        form = UserInfoPasswordModelForm(data=request.POST)

        if form.is_valid():
            user_obj.password = get_md5(form.cleaned_data['password'])
            user_obj.save()

            return redirect(self.reverse_list_url())
        return render(request, 'stark/change.html', {'form': form})

    list_display = ['name', 'nickname', get_choice_text('性别', 'gender'), 'phone', 'email', 'depart',
                    display_reset_password, Handler.display_edit, Handler.display_del]