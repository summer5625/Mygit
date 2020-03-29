# -*- coding: utf-8 -*-
# @Time    : 2020/2/14  13:15
# @Author  : XiaTian
# @File    : check_payment_record.py
from django.urls import path
from stark.service.handle_table import Handler, SearchOption, get_choice_text, get_datetime_text
from .base import PermissionHandler


class CheckPaymentHandler(PermissionHandler, Handler):

    order_list = ['-id', 'confirm_status']
    search_list = ['consultant__nickname__contains', 'class_list__course__title__contains', 'customer__name__contains']
    search_group = [SearchOption('pay_type'), SearchOption('confirm_status')]

    def get_urls(self):
        
        patterns = [
            path('list/', self.wrapper(self.list_view), name=self.get_list_url_name),
        ]

        patterns.extend(self.extra_urls())

        return patterns

    def action_multi_check(self, request, *args, **kwargs):

        pk_list = request.POST.getlist('pk')

        for pk in pk_list:

            payment_obj = self.model_class.objects.filter(id=pk, confirm_status=1).first()

            if not payment_obj:
                continue
            payment_obj.confirm_status = 2
            payment_obj.save()

            payment_obj.customer.status_choices = 1
            payment_obj.customer.save()

            payment_obj.customer.student.student_status = 2
            payment_obj.customer.student.save()

    action_multi_check.text = '批量确认'
    
    def action_multi_cancel(self, request, *args, **kwargs):

        pk_list = request.POST.getlist('pk')
        self.model_class.objects.filter(id__in=pk_list, confirm_status=1).update(confirm_status=3)
    
    action_multi_cancel.text = '批量驳回'
    action_list = [action_multi_check, action_multi_cancel]
    list_display = [Handler.display_checkbox, 'customer', get_choice_text('费用类型', 'pay_type'), 'paid_fee',
                    'class_list', get_datetime_text('缴费日期', 'apply_date'), get_choice_text('状态', 'confirm_status'),
                    'consultant']
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    