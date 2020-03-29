# -*- coding: utf-8 -*-
# @Time    : 2019/11/14  23:09
# @Author  : XiaTian
# @File    : user.py

from django import forms
from django.core.exceptions import ValidationError
from rbac.forms.base import BootStrapModelForm
from rbac import models


class UpdateUserInfoModelForm(BootStrapModelForm):
    
    class Meta:
        
        model = models.UserInfo
        fields = ['name', 'email', 'roles']


class UserInfoModelForm(BootStrapModelForm):
    
    confirm_password = forms.CharField(label='确认密码')

    class Meta:
        model = models.UserInfo
        fields = ['name', 'password', 'email', 'confirm_password']

    def clean_confirm_password(self):
        '''
        两次输入密码一致性验证
        :return:
        '''

        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError('两次密码不一致!')

        return confirm_password


class ResetPasswordUserModelForm(BootStrapModelForm):

    confirm_password = forms.CharField(label='确认密码')

    class Meta:
        model = models.UserInfo
        fields = ['password', 'confirm_password']

    def clean_confirm_password(self):
        '''
        两次输入密码一致性验证
        :return:
        '''

        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError('两次密码不一致!')

        return confirm_password















