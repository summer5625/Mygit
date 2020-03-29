# -*- coding: utf-8 -*-
# @Time    : 2019/11/1  22:29
# @Author  : XiaTian
# @File    : depart.py


from django import forms
from app01 import models


class DepartmentModelForm(forms.ModelForm):
    class Meta:
        model = models.Department
        fields = ['title', ]

    # 统一给表单的每一项增加统一样式
    def __init__(self, *args, **kwargs):
        super(DepartmentModelForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
