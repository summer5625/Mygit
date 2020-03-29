# -*- coding: utf-8 -*-
# @Time    : 2019/11/12  22:37
# @Author  : XiaTian
# @File    : course_record.py

from django.urls import re_path, path
from django.shortcuts import HttpResponse, render, reverse
from django.utils.safestring import mark_safe
from django.forms.models import modelformset_factory

from stark.service.handle_table import Handler, StarkModelForm, get_datetime_text
from web import models
from .base import PermissionHandler


class CourseRecordModelForm(StarkModelForm):
    class Meta:
        model = models.CourseRecord
        fields = ['day_num', 'teacher']


class StudentRecordModelForm(StarkModelForm):
    
    class Meta:
        
        model = models.StudyRecord
        fields = ['record']
    

class ClassRecordHandler(PermissionHandler, Handler):
    has_add_btn = True

    model_form_class = CourseRecordModelForm

    def get_urls(self):
        patterns = [
            re_path(r'^list/(?P<class_id>\d+)/$', self.wrapper(self.list_view), name=self.get_list_url_name),
            re_path(r'add/(?P<class_id>\d+)/$', self.wrapper(self.add_view), name=self.get_add_url_name),
            re_path(r'^edit/(?P<class_id>\d+)/(?P<pk>\d+)/$', self.wrapper(self.edit_view),
                    name=self.get_edit_url_name),
            re_path(r'^del/(?P<class_id>\d+)/(?P<pk>\d+)/$', self.wrapper(self.del_view), name=self.get_del_url_name),
            re_path(r'^attendance/(?P<course_record_id>\d+)/$', self.wrapper(self.attendance_view),
                name=self.get_url_name('attendance')),
        ]

        patterns.extend(self.extra_urls())

        return patterns

    def action_multi_init(self, request, *args, **kwargs):
        course_record_id_list = request.POST.getlist('pk')  # 选择的考勤记录id
        class_id = kwargs.get('class_id')
        class_obj = models.ClassList.objects.filter(id=class_id).first()

        if not class_obj:
            return HttpResponse('班级不存在!')
        student_obj_list = class_obj.student_set.all()  # 反向关联，查询班级的学生

        for course_record in course_record_id_list:

            # 判断对应班级的上课记录是否存在
            course_record_obj = models.CourseRecord.objects.filter(id=course_record, class_object_id=class_id).first()

            if not course_record_obj:
                continue

            # 判断对应的考勤记录是否存在
            student_record_obj = models.StudyRecord.objects.filter(course_record=course_record_obj).exists()
            if student_record_obj:
                continue

            # 创建考勤记录
            student_record_obj_list = [models.StudyRecord(student_id=stu.id, course_record_id=course_record) for stu in
                                       student_obj_list]

            models.StudyRecord.objects.bulk_create(student_record_obj_list, batch_size=50)

        return

    action_multi_init.text = '批量初始化考勤'

    action_list = [action_multi_init]

    def get_queryset(self, request, *args, **kwargs):
        class_id = kwargs.get('class_id')

        return self.model_class.objects.filter(class_object_id=class_id)

    def save(self, request, form, is_update, *args, **kwargs):
        class_id = kwargs.get('class_id')

        if not is_update:
            form.instance.class_object_id = class_id

        form.save()

    def display_attendance(self, obj=None, is_header=None, *args, **kwargs):

        if is_header:

            return '考勤'
        name = '%s:%s' % (self.stark_site.namespace, self.get_url_name('attendance'))
        attendance_url = reverse(name, kwargs={'course_record_id': obj.pk})
        
        return mark_safe("<a target='_blank' href='%s'>考勤</a>" % attendance_url)
    
    def attendance_view(self, request, course_record_id, *args, **kwargs):

        student_record_obj_list = models.StudyRecord.objects.filter(course_record_id=course_record_id)
        student_model_formset = modelformset_factory(models.StudyRecord, form=StudentRecordModelForm, extra=0)

        if request.method == 'POST':
            formset = student_model_formset(queryset=student_record_obj_list, data=request.POST)

            if formset.is_valid():
                formset.save()

            return render(request, 'attendance.html', {'formset': formset})

        formset = student_model_formset(queryset=student_record_obj_list)

        return render(request, 'attendance.html', {'formset': formset})

    list_display = [
        Handler.display_checkbox,
        'class_object',
        'day_num',
        'teacher',
        get_datetime_text('时间', 'date'),
        display_attendance,
        Handler.display_edit,
        Handler.display_del
    ]












