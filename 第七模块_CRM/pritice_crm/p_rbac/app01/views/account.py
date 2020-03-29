# -*- coding: utf-8 -*-
# @Time    : 2019/11/15  14:27
# @Author  : XiaTian
# @File    : account.py

from django.shortcuts import render, redirect

from rbac import models
from rbac.service.init_permission import init_permission


def login(request):

    if request.method == 'GET':

        return render(request, 'login.html')

    user = request.POST.get('user')
    pwd = request.POST.get('pwd')

    current_user = models.UserInfo.objects.filter(name=user, password=pwd).first()

    if not current_user:
        return render(request, 'login.html', {'msg': '用户名或密码错误!'})

    init_permission(request, current_user)

    return redirect('/index/')


def logout(request):
    
    request.session.flush()

    return redirect('/login/')


def index(request):
    
    return render(request, '1、vue起步.html')