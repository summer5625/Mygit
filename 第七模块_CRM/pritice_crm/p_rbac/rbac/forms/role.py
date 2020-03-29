# -*- coding: utf-8 -*-
# @Time    : 2019/11/14  23:09
# @Author  : XiaTian
# @File    : role.py

from rbac.forms.base import BootStrapModelForm
from django.core.exceptions import ValidationError
from rbac.models import Role


class RoleModelForm(BootStrapModelForm):

    class Meta:
        model = Role
        fields = ['title']

    def clean_title(self):

        val =self.cleaned_data.get('title')
        ret = Role.objects.filter(title=val).first()

        if not ret:
            return val

        raise ValidationError('角色名称重复!')
