# -*- coding: utf-8 -*-
# @Time    : 2020/1/30  19:23
# @Author  : XiaTian
# @File    : base.py
from django import forms


class BootStrapModelForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(BootStrapModelForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'