# -*- coding: utf-8 -*-
# @Time    : 2019/11/14  23:09
# @Author  : XiaTian
# @File    : base.py

from django import forms


class BootStrapModelForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        
        super(BootStrapModelForm, self).__init__(*args, **kwargs)

        for name, filed in self.fields.items():

            filed.widget.attrs['class'] = 'form-control'
        
    