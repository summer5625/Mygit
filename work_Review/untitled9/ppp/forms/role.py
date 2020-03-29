# -*- coding: utf-8 -*-
# @Time    : 2020/1/29  19:37
# @Author  : XiaTian
# @File    : role.py
from django import forms
from django.core.exceptions import ValidationError
from ppp import models


class RoleModelForm(forms.ModelForm):

    class Meta:
        model = models.Role
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})
        }
        error_messages = {
            'title': {'required': '不能为空!'},
        }

    def clean_title(self):

        val = self.cleaned_data.get('title')

        ret = models.Role.objects.filter(title=val)
        if not ret:
            return val
        
        else:
            raise ValidationError('角色名称重复')