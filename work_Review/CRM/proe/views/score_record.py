# -*- coding: utf-8 -*-
# @Time    : 2020/2/13  17:25
# @Author  : XiaTian
# @File    : score_record.py
from django.urls import re_path
from stark.service.handle_table import Handler, StarkModelForm
from proe import models
from .base import PermissionHandler


class ScoreModel(StarkModelForm):
    
    class Meta:
        
        model = models.ScoreRecord
        fields =['content', 'score']
        
        
class ScoreHandler(PermissionHandler, Handler):

    has_add_btn = True
    list_display = ['content', 'score', 'user']
    model_form_class = ScoreModel
    
    def get_urls(self):
        
        patterns = [
            re_path(r'^list/(?P<student_id>\d+)/$', self.wrapper(self.list_view), name=self.get_list_url_name),
            re_path(r'^add/(?P<student_id>\d+)/$', self.wrapper(self.add_view), name=self.get_add_url_name)
        ]
        
        patterns.extend(self.extra_urls())
        
        return patterns
    
    def get_queryset(self, request, *args, **kwargs):

        student_id = kwargs.get('student_id')
        
        return self.model_class.objiects.filter(student_id=student_id)
    
    def save(self, request, form, is_update, *args, **kwargs):
        
        current_user_id = request.session['user_info']['id']
        student_id = kwargs.get('student_id')
        
        form.instance.student_id = student_id
        form.instance.user_id = current_user_id
        form.save()
        
        score = form.instance.score
        
        if score > 0:
            
            form.instance.student.score += abs(score)
        else:
            form.instance.score -= abs(score)
        
        form.instance.student.save()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    