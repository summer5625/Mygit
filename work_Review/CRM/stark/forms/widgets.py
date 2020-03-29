# -*- coding: utf-8 -*-
# @Time    : 2019/11/9  17:52
# @Author  : XiaTian
# @File    : widgets.py

from django import forms


class DateTimePicker(forms.TextInput):
    
    template_name = 'stark/forms/widgets/datetime_picker.html'
