# -*- coding: utf-8 -*-
# @Time    : 2019/11/11  16:42
# @Author  : XiaTian
# @File    : consultant_record.py

from django.urls import re_path
from django.shortcuts import HttpResponse

from stark.service.handle_table import Handler, StarkModelForm
from web import models
from .base import PermissionHandler


class ConsultantRecordAddModelForm(StarkModelForm):
    class Meta:
        model = models.ConsultRecord
        fields = ['note']


class ConsultantRecordHandler(PermissionHandler, Handler):
    has_add_btn = True

    list_display = [
        'note',
        'consultant',
        'date',
        Handler.display_edit,
        Handler.display_del]

    list_template = ['consult_record.html']

    model_form_class = ConsultantRecordAddModelForm

    def get_urls(self):
        '''
        生成url
        :return:
        '''

        # url别名设置

        patterns = [
            re_path(r'^list/(?P<customer_id>\d+)/$', self.wrapper(self.list_view), name=self.get_list_url_name),
            re_path(r'add/(?P<customer_id>\d+)/$', self.wrapper(self.add_view), name=self.get_add_url_name),
            re_path(r'^edit/(?P<customer_id>\d+)/(?P<pk>\d+)/$', self.wrapper(self.edit_view), name=self.get_edit_url_name),
            re_path(r'^del/(?P<customer_id>\d+)/(?P<pk>\d+)/$', self.wrapper(self.del_view), name=self.get_del_url_name)
        ]

        patterns.extend(self.extra_urls())

        return patterns

    def get_queryset(self, request, *args, **kwargs):

        current_user_id = request.session['user_info']['id']
        customer_id = kwargs.get('customer_id')

        return self.model_class.objects.filter(
            customer_id=customer_id, consultant_id=current_user_id)

    def change_object(self, request, pk, *args, **kwargs):

        current_user_id = request.session['user_info']['id']
        customer_id = kwargs.get('customer_id')
        obj = models.ConsultRecord.objects.filter(
            pk=pk,
            customer_id=customer_id,
            customer__consultant_id=current_user_id).first()
        return obj

    def del_object(self, request, pk, *args, **kwargs):

        current_user_id = request.session['user_info']['id']
        customer_id = kwargs.get('customer_id')
        del_obj = models.ConsultRecord.objects.filter(
            pk=pk,
            customer_id=customer_id,
            customer__consultant_id=current_user_id)

        if not del_obj.exists():
            return HttpResponse('要删除的记录不在，请重新选择!')

        del_obj.delete()

    def save(self, request, form, is_update, *args, **kwargs):
        current_user_id = request.session['user_info']['id']
        customer_id = kwargs.get('customer_id')
        obj_exists = models.Customer.objects.filter(
            id=customer_id, consultant_id=current_user_id).exists()

        if not obj_exists:
            return HttpResponse('非法操作!')

        if not is_update:
            form.instance.customer_id = customer_id
            form.instance.consultant_id = current_user_id
        form.save()
