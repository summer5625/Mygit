# -*- coding: utf-8 -*-
# @Time    : 2019/10/26  21:12
# @Author  : XiaTian
# @File    : role.py

from django import forms
from django.core.exceptions import ValidationError
from rbac import models


class RoleModelForm(forms.ModelForm):

    class Meta:
        model = models.Role
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'})

        }
        error_messages = {
            'title': {"required": '不能为空!'},
        }

    def clean_title(self):
        '''
        校验职位名称是否重复
        :return:
        '''

        val = self.cleaned_data.get('title')

        ret = models.Role.objects.filter(title=val)

        if not ret:
            
            return val
        
        else:
            
            raise ValidationError('职位名称重复!')