# -*- coding: utf-8 -*-
# @Time    : 2019/11/15  14:27
# @Author  : XiaTian
# @File    : customer.py

from django import forms
from app01 import models


class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
