# -*- coding: utf-8 -*-
# @Time    : 2019/11/12  20:21
# @Author  : XiaTian
# @File    : student.py

from django.urls import path, re_path, reverse
from django.utils.safestring import mark_safe

from stark.service.handle_table import Handler, StarkModelForm, get_choice_text, get_m2m_text, SearchOption
from web import models
from .base import PermissionHandler


class StudentModelForm(StarkModelForm):
    class Meta:
        model = models.Student
        fields = ['qq', 'mobile', 'emergency_contract', 'memo']


class StudentHandler(PermissionHandler, Handler):
    model_form_class = StudentModelForm

    search_list = ['qq__contains', 'mobile__contains', 'customer__name__contains']

    search_group = [SearchOption('class_list', text_func=lambda x: '%s-%s' % (x.school.title, str(x)))]

    def display_score(self, obj=None, is_header=None, *args, **kwargs):
        if is_header:
            return '积分管理'
        record_url = reverse('stark:web_scorerecord_list', kwargs={'student_id': obj.pk})
        return mark_safe("<a target='_blank' href='%s'>%s</a>" % (record_url, obj.score))

    def get_urls(self):
        patterns = [
            path(r'list/', self.wrapper(self.list_view), name=self.get_list_url_name),
            re_path(r'^edit/(?P<pk>\d+)/$', self.wrapper(self.edit_view), name=self.get_edit_url_name)
        ]

        patterns.extend(self.extra_urls())

        return patterns

    list_display = ['customer', 'qq', 'mobile', 'emergency_contract', get_m2m_text('已报班级', 'class_list'),
                    display_score, get_choice_text('状态', 'student_status'), Handler.display_edit]


