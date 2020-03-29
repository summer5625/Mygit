# -*- coding: utf-8 -*-
# @Time    : 2019/11/1  22:03
# @Author  : XiaTian
# @File    : host.py

from django import forms
from app01 import models


class HostModelForm(forms.ModelForm):
    
    class Meta:
        
        model = models.Host
        fields = ['hostname', 'ip', 'depart']

    # 统一给表单的每一项增加统一样式
    def __init__(self, *args, **kwargs):
        super(HostModelForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        