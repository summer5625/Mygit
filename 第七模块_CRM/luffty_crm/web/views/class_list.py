# -*- coding: utf-8 -*-
# @Time    : 2019/11/9  15:43
# @Author  : XiaTian
# @File    : class_list.py

from django.urls import reverse
from django.utils.safestring import mark_safe
from stark.service.handle_table import Handler, get_datetime_text, get_m2m_text, StarkModelForm, SearchOption
from stark.forms.widgets import DateTimePicker
from web import models
from .base import PermissionHandler


class ClassListModelForm(StarkModelForm):
    
    class Meta:
        model = models.ClassList
        fields = '__all__'
        widgets = {
            'start_date': DateTimePicker,
            'graduate_date': DateTimePicker
        }


class ClassListHandler(PermissionHandler, Handler):

    has_add_btn = True
    model_form_class = ClassListModelForm
    search_list = ['school__title__contains', 'course__title__contains',]
    search_group = [SearchOption('school'), SearchOption('course')]

    def display_class(self, obj=None, is_header=None, *args, **kwargs):
        if is_header:
            return '班级'
        return '%s %s期' % (obj.course.title, obj.semester)

    def display_class_record(self, obj=None, is_header=None, *args, **kwargs):
        if is_header:
            return '上课记录'
        record_url = reverse('stark:web_courserecord_list', kwargs={'class_id': obj.pk})
        return mark_safe("<a target='_blank' href='%s'>上课记录</a>" % record_url)

    list_display = ['school', display_class, 'price', get_datetime_text('开班日期', 'start_date'), 'class_teacher',
                    get_m2m_text('任课老师', 'tec_teacher'), display_class_record, Handler.display_edit, Handler.display_del]
