# -*- coding: utf-8 -*-
# @Time    : 2019/11/9  21:21
# @Author  : XiaTian
# @File    : private_customer.py

from django.urls import path, re_path, reverse
from django.utils.safestring import mark_safe

from stark.service.handle_table import Handler, StarkModelForm, get_choice_text
from web import models
from .base import PermissionHandler


class PrivateCustomerModelForm(StarkModelForm):
    class Meta:
        model = models.Customer
        exclude = ['consultant', ]


class PrivateCustomerHandler(PermissionHandler, Handler):
    has_add_btn = True
    model_form_class = PrivateCustomerModelForm

    def display_record(self, obj=None, is_header=None, *args, **kwargs):

        if is_header:
            return '跟进'
        record_url = reverse('stark:web_consultrecord_list', kwargs={'customer_id': obj.pk})
        return mark_safe("<a target='_blank' href='%s'>跟进</a>" % record_url)

    def display_payment_record(self, obj=None, is_header=None, *args, **kwargs):

        if is_header:
            return '缴费'
        record_url = reverse('stark:web_paymentrecord_list', kwargs={'customer_id': obj.pk})
        return mark_safe("<a target='_blank' href='%s'>缴费</a>" % record_url)

    def get_queryset(self, request, *args, **kwargs):

        current_user_id = request.session['user_info']['id']

        return self.model_class.objects.filter(consultant_id=current_user_id)

    def save(self, request, form, is_update, *args, **kwargs):

        current_user_id = request.session['user_info']['id']
        form.instance.consultant_id = current_user_id
        form.save()

    def action_multi_remove(self, request, *args, **kwargs):
        '''
        批量移除到公户
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''

        current_user_id = request.session['user_info']['id']
        pk_list = request.POST.getlist('pk')
        self.model_class.objects.filter(id__in=pk_list, consultant_id=current_user_id).update(consultant_id=None)

    action_multi_remove.text = '批量移除到公户'

    action_list = [action_multi_remove, ]
    list_display = [Handler.display_checkbox, 'name', 'contact', get_choice_text('状态', 'status'), display_record,
                    display_payment_record, Handler.display_edit, Handler.display_del]
