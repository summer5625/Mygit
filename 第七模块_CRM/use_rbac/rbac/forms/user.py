# -*- coding: utf-8 -*-
# @Time    : 2019/10/27  16:39
# @Author  : XiaTian
# @File    : user.py

import re
from django import forms
from django.core.exceptions import ValidationError
from rbac import models


class UserModelForm(forms.ModelForm):

    confirm_password = forms.CharField(label='确认密码') # 给表单新增字段
    class Meta:

        model = models.UserInfo
        fields = ['name', 'password', 'email', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput(),
            'confirm_password': forms.PasswordInput(),
        }

    # 统一给表单的每一项增加统一样式
    def __init__(self, *args, **kwargs):

        super(UserModelForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

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

    def clean_name(self):
        '''
        验证用户名是否重复
        :return:
        '''
        name = self.cleaned_data.get('name')
        user_obj = models.UserInfo.objects.filter(name=name)

        if user_obj:

            raise ValidationError('用户名重复!')

        return name

    def clean_email(self):
        '''
        校验邮箱格式是否正确，是否被注册过
        :return:
        '''
        email = self.cleaned_data.get('email')
        email_obj = models.UserInfo.objects.filter(email=email)
        match_chr = re.fullmatch('\w+@\w+\.(com|cn|edu)', email)

        if not match_chr:

            raise ValidationError('邮箱格式不正确!')

        if email_obj:

            raise ValidationError('邮箱被注册过!')

        return email


class ResetPasswordUserModelForm(forms.ModelForm):
    
    confirm_password = forms.CharField(label='确认密码')
    
    class Meta:
    
        model = models.UserInfo

        fields = ['password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput(),
            'confirm_password': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super(ResetPasswordUserModelForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

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
            
            
class UpdateUserModelForm(forms.ModelForm):

    class Meta:
        model = models.UserInfo
        fields = ['name', 'email']

    def __init__(self, *args, **kwargs):
        super(UpdateUserModelForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        '''
        验证用户名是否重复
        :return:
        '''
        name = self.cleaned_data.get('name')
        user_obj = models.UserInfo.objects.filter(name=name)

        if user_obj:

            raise ValidationError('用户名重复!')

        return name

    def clean_email(self):
        '''
        校验邮箱格式是否正确，是否被注册过
        :return:
        '''
        email = self.cleaned_data.get('email')
        email_obj = models.UserInfo.objects.filter(email=email)
        match_chr = re.fullmatch('\w+@\w+\.(com|cn|edu)', email)

        if not match_chr:

            raise ValidationError('邮箱格式不正确!')

        if email_obj:

            raise ValidationError('邮箱被注册过!')

        return email