# -*- coding: utf-8 -*-
# @Time    : 2019/11/12  13:41
# @Author  : XiaTian
# @File    : payment_record.py

from django.urls import re_path
from django.shortcuts import HttpResponse
from django import forms

from stark.service.handle_table import Handler, StarkModelForm, get_choice_text, get_datetime_text
from web import models
from .base import PermissionHandler


class PaymentModelForm(StarkModelForm):
    class Meta:
        model = models.PaymentRecord
        fields = ['pay_type', 'paid_fee', 'class_list', 'note']


class StudentPaymentRecordModelForm(StarkModelForm):
    qq = forms.CharField(label='QQ号', max_length=32)
    mobile = forms.CharField(label='电话', max_length=32)
    emergency_contract = forms.CharField(label='紧急联系人电话', max_length=32)

    class Meta:
        model = models.PaymentRecord
        fields = ['pay_type', 'paid_fee', 'class_list', 'qq', 'mobile', 'emergency_contract', 'note']


class PayRecordHandler(PermissionHandler, Handler):
    has_add_btn = True

    def get_list_display(self, request, *args, **kwargs):
        '''
        获取页面上应该显示的列，预留自定义扩展
        :return:
        '''

        value = []
        if self.list_display:
            value.extend(self.list_display)
        return value

    def get_urls(self):

        patterns = [
            re_path(r'^list/(?P<customer_id>\d+)/$', self.wrapper(self.list_view), name=self.get_list_url_name),
            re_path(r'^add/(?P<customer_id>\d+)/$', self.wrapper(self.add_view), name=self.get_add_url_name),
        ]

        patterns.extend(self.extra_urls())

        return patterns

    def get_queryset(self, request, *args, **kwargs):

        current_user_id = request.session['user_info']['id']
        customer_id = kwargs.get('customer_id')
        obj = self.model_class.objects.filter(customer__consultant_id=current_user_id, customer_id=customer_id)

        return obj

    def get_model_form_class(self, is_add, request, pk, *args, **kwargs):
        # 如果当前客户有学生信息，则使用PaymentModelForm；否则StudentPaymentRecordModelForm

        customer_id = kwargs.get('customer_id')
        student_exists = models.Student.objects.filter(customer_id=customer_id).exists()
        if not student_exists:
            return StudentPaymentRecordModelForm

        return PaymentModelForm

    def save(self, request, form, is_update, *args, **kwargs):

        current_user_id = request.session['user_info']['id']
        customer_id = kwargs.get('customer_id')

        obj_exists = models.Customer.objects.filter(id=customer_id, consultant_id=current_user_id).exists()

        if not obj_exists:
            return HttpResponse('非法操作')

        form.instance.customer_id = customer_id
        form.instance.consultant_id = current_user_id
        form.save()

        # 创建学员信息
        class_list = form.cleaned_data['class_list']
        fetch_student = models.Student.objects.filter(customer_id=customer_id).first()

        if not fetch_student:
            qq = form.cleaned_data['qq']
            mobile = form.cleaned_data['mobile']
            emergency_contract = form.cleaned_data['emergency_contract']
            student_object = models.Student.objects.create(qq=qq, mobile=mobile, emergency_contract=emergency_contract,
                                                           customer_id=customer_id)

            student_object.class_list.add(class_list.id)  # 绑定多对多关系
        else:
            fetch_student.class_list.add(class_list.id)

    list_display = [get_choice_text('费用类型', 'pay_type'), 'paid_fee', 'class_list',
                    get_datetime_text('申请日期', 'apply_date'), 'consultant',
                    get_choice_text('状态', 'confirm_status')]
