# -*- coding: utf-8 -*-
# @Time    : 2019/10/17  14:07
# @Author  : XiaTian
# @File    : MyForm.py

from django.forms import widgets
from django.core.exceptions import ValidationError
from django import forms


from blog.models import *


class UserForm(forms.Form):
    
    user = forms.CharField(
        min_length=5,
        label='用户名',
        error_messages={
            'required': '该字段不能为空',
            'invalid': '长度不够，至少5个字符'},
        widget=widgets.TextInput(attrs={'class': "form-control"}))
    
    pwd = forms.CharField(
        label='密码',
        error_messages={'required': '该字段不能为空'},
        widget=widgets.PasswordInput(attrs={'class': "form-control"}))
    
    r_pwd = forms.CharField(
        label='确认密码',
        error_messages={'required': '该字段不能为空'},
        widget=widgets.PasswordInput(attrs={'class': "form-control"}))
    
    email = forms.EmailField(
        label='邮箱',
        error_messages={
            'required': '该字段不能为空',
            'invalid': '邮箱格式错误'},
        widget=widgets.TextInput(attrs={'class': "form-control"}))
    
    tel = forms.CharField(
        label='电话',
        error_messages={'required': '该字段不能为空'},
        widget=widgets.TextInput(attrs={'class': "form-control"}))

    def clean_user(self):

        user = self.cleaned_data.get('user')

        ret = UserInfo.objects.filter(username=user)

        if not ret:

            if len(user) >= 5:

                return user

            else:

                raise ValidationError('用户名长度要求 5-50 位')
        
        else:
            
            raise ValidationError('用户名已被注册!')

    def clean_tel(self):

        tel = self.cleaned_data.get('tel')

        if len(tel) == 11:
            
            return tel
        
        else:
            
            raise ValidationError('手机号码格式错误!')

    # def clean_pwd(self):
    #
    #     pwd = self.cleaned_data.get('pwd')
    #
    #     if len(pwd) >= 6:
    #
    #         if not pwd.isalpha() and not pwd.isdigit():
    #
    #             return pwd
    #
    #         else:
    #
    #             raise ValidationError('密码必须包含字母和数字的组合')
    #
    #     else:
    #
    #         raise ValidationError('密码长度要求 8-50 位')

    def clean(self):

        pwd = self.cleaned_data.get('pwd')
        r_pwd = self.cleaned_data.get('r_pwd')
        
        if pwd and r_pwd:
            
            if pwd == r_pwd:
                
                return self.cleaned_data
            
            else:
                
                raise ValidationError('两次密码不一致!')
        else:
            
            return self.cleaned_data
            


        















