# -*- coding: utf-8 -*-
# @Time    : 2019/11/15  14:27
# @Author  : XiaTian
# @File    : payment.py

from django import forms
from app01 import models


class PaymentForm(forms.ModelForm):
    class Meta:
        model = models.Payment
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
        self.fields['customer'].empty_label = "请选择客户"


class PaymentUserForm(forms.ModelForm):
    class Meta:
        model = models.Payment
        exclude = ['customer',]

    def __init__(self, *args, **kwargs):
        super(PaymentUserForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
