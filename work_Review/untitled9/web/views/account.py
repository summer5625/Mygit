# -*- coding: utf-8 -*-
# @Time    : 2020/1/29  13:26
# @Author  : XiaTian
# @File    : account.py
from django.shortcuts import render, redirect, reverse
from ppp import models
from ppp.service.init_permission import init_permission


def login(request):
    
    if request.method == 'GET':
        return render(request, 'login.html')
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    
    current_user = models.UserInfo.objects.filter(name=user, password=pwd).first()

    if not current_user:
        return render(request, 'login.html', {'msg': '用户名或密码错误'})
  
    init_permission(request, current_user)

    return redirect(reverse('ppp:menu_list'))


def logout(request):

    request.session.flush()
    
    return redirect('/login/')












