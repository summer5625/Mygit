# -*- coding: utf-8 -*-
# @Time    : 2019/11/9  21:20
# @Author  : XiaTian
# @File    : public_customer.py

from django.utils.safestring import mark_safe
from django.urls import re_path
from django.shortcuts import HttpResponse, render
from django.db import transaction  # 添加数据库事务

from stark.service.handle_table import Handler, get_m2m_text, StarkModelForm, get_choice_text
from web import models
from .base import PermissionHandler


class PublicCustomerModelForm(StarkModelForm):
    class Meta:
        model = models.Customer
        exclude = ['consultant', ]


class PublicCustomerHandler(PermissionHandler, Handler):
    has_add_btn = True

    model_form_class = PublicCustomerModelForm

    def get_queryset(self, request, *args, **kwargs):
        return self.model_class.objects.filter(consultant__isnull=True)

    def display_record(self, obj=None, is_header=None, *args, **kwargs):

        if is_header:
            return '跟进记录'
        record_url = self.reverse_common_url(self.get_url_name('record_view'), pk=obj.pk)
        return mark_safe("<a href='%s'>查看跟进记录</a>" % record_url)

    def record_view(self, request, pk, *args, **kwargs):
        '''
        查看跟进记录
        :return:
        '''

        record_list = models.ConsultRecord.objects.filter(customer_id=pk)

        return render(request, 'record.html', {'record_list': record_list})

    def extra_urls(self):
        patterns = [re_path(r'^record/(?P<pk>\d+)/$', self.wrapper(self.record_view),
                            name=self.get_url_name('record_view'))]
        return patterns

    def action_multi_apply(self, request, *args, **kwargs):
        '''
        批量申请到私户
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''

        current_user = request.session['user_info']['id']

        pk_list = request.POST.getlist('pk')

        # 用户私户中未转化的客户数量
        private_customer_count = models.Customer.objects.filter(consultant_id=current_user, status=2).count()

        # 对私户中未转化的客户数量限制
        if private_customer_count + len(pk_list) > 150:
            return HttpResponse('客户数量超标，私户中已经有了%s个客户，最多再能添加%s个客户' % (
                private_customer_count, 150 - private_customer_count
            ))

        # 数据库中加事务锁，防止两个人同时申请同一个客户造成混乱
        flag = False
        with transaction.atomic():
            # 在数据库中加锁
            origin_queryset = models.Customer.objects.filter(id__in=pk_list, status=2,
                                                             consultant__isnull=True).select_for_update()

            if len(origin_queryset) == len(pk_list):
                models.Customer.objects.filter(id__in=pk_list, status=2, consultant__isnull=True).update(
                    consultant_id=current_user)
                flag = True

        if not flag:
            return HttpResponse('手速太慢')

    action_multi_apply.text = '批量申请到私户'

    action_list = [action_multi_apply, ]

    list_display = [Handler.display_checkbox, 'name', 'contact', get_choice_text('状态', 'status'),
                    get_m2m_text('咨询课程', 'course'),
                    display_record, Handler.display_edit, Handler.display_del]
