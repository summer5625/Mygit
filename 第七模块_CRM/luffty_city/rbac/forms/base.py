# -*- coding: utf-8 -*-
# @Time    : 2019/10/28  21:47
# @Author  : XiaTian
# @File    : base.py

from django import forms


# 定制form表单样式的基类
class BootStrapModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        super(BootStrapModelForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            