# -*- coding: utf-8 -*-
# @Time    : 2020/1/28  18:15
# @Author  : XiaTian
# @File    : user.py
import re
from django import forms
from django.core.exceptions import ValidationError
from ppp import models


class UserModelFrom(forms.ModelForm):

    confirm_password = forms.CharField(label='确认密码')

    class Meta:

        model = models.UserInfo
        fields = ['name', 'password', 'email', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput(),
            'confirm_password': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        
        super(UserModelFrom, self).__init__(*args, **kwargs)
        for name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'form-control'

    def clean_confirm_password(self):
        
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError('两次密码不一致')

        return confirm_password

    def clean_name(self):

        name = self.cleaned_data.get('name')
        user_obj = models.UserInfo.objects.filter(name=name)

        if user_obj:
            raise ValidationError('用户名重复')
        return name

    def clean_email(self):

        email = self.cleaned_data.get('email')
        email_obj = models.UserInfo.objects.filter(email=email)
        match_chr = re.fullmatch('\w+@\w+\.(com|cn|edu)', email)

        if email_obj:
            raise ValidationError('邮箱已被注册过')
        if not match_chr:
            raise ValidationError('邮箱格式不正确')
        return email
    

class ResetPassword(forms.ModelForm):

    confirm_password = forms.CharField(label='确认密码')

    class Meta:
        model = models.UserInfo
        fields = ['password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput(),
            'confirm_password': forms.PasswordInput(),
        }
    
    def __init__(self, *args, **kwargs):
        
        super(ResetPassword, self).__init__(*args, **kwargs)

        for name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'form-control'
            
    def clean_confirm_password(self):

        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError('两次密码不一致')
        return confirm_password


class UpdateUser(forms.ModelForm):

    class Meta:
        model = models.UserInfo
        fields = ['name', 'email']

    def __init__(self, *args, **kwargs):

        super(UpdateUser, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    # def clean_name(self):
    #
    #     name = self.cleaned_data.get('name')
    #     user_obj = models.UserInfo.objects.filter(name=name)
    #
    #     if user_obj:
    #         raise ValidationError('用户名重复')
    #     return name

    def clean_email(self):

        email = self.cleaned_data.get('email')
        email_obj = models.UserInfo.objects.filter(email=email)
        match_chr = re.fullmatch('\w+@\w+\.(com|cn|edu)', email)

        if not match_chr:
            raise ValidationError('邮箱格式不正确!')

        # if email_obj:
        #     raise ValidationError('邮箱被注册过!')

        return email
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            























