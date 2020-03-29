# -*- coding: utf-8 -*-
# @Time    : 2020/2/13  18:25
# @Author  : XiaTian
# @File    : public_customer.py
from django.utils.safestring import mark_safe
from django.urls import re_path
from django.shortcuts import HttpResponse, render
from django.db import transaction
from stark.service.handle_table import Handler, StarkModelForm, get_choice_text, get_m2m_text
from proe import models
from .base import PermissionHandler


class PublicCustomerModel(StarkModelForm):
    
    class Meta:
        model = models.Customer
        exclude = ['consultant']
        

class PublicCustomerHandler(PermissionHandler, Handler):

    has_add_btn = True
    model_form_class = PublicCustomerModel
    
    def get_queryset(self, request, *args, **kwargs):

        return self.model_class.objects.filter(consultant__isnull=True)

    def display_record(self, obj=None, is_header=None, *args, **kwargs):

        if is_header:
            return '跟进记录'
        
        record_url = self.reverse_common_url(self.get_url_name('record_view'), pk=obj.pk)
        return mark_safe("<a href='%s'>查看跟进记录</a>" % record_url)
    
    def record_view(self, request, pk, *args, **kwargs):

        record_list = models.ConsultRecord.objects.filter(customer_id=pk)
        return render(request, 'record.html', {'record_list': record_list})
    
    def extra_urls(self):

        patterns = [
            re_path(r'^record/(?P<pk>\d+)/$', self.wrapper(self.record_view), name=self.get_url_name('record_view'))
        ]
        
        return patterns
    
    def action_multi_apply(self, request, *args, **kwargs):

        current_user = request.session['user_info']['id']
        pk_list = request.POST.get('pk')
        private_customer_count = models.Customer.objects.filter(consultant_id=current_user, status=2).count()
        
        if private_customer_count + len(pk_list) > 150:
            
            return HttpResponse('客户数量超标，私户中已经有了%s个客户，最多再能添加%s个客户' % 
                                (private_customer_count, 150 - private_customer_count))
        
        flag = False
        with transaction.atomic():
            
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
                    get_m2m_text('咨询课程', 'course'), display_record, Handler.display_edit, Handler.display_del]




















