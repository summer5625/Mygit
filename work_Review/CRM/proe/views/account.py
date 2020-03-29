# -*- coding: utf-8 -*-
# @Time    : 2020/2/13  12:52
# @Author  : XiaTian
# @File    : account.py
from django.shortcuts import render, redirect
from proe import models
from proe.utils.md5 import get_md5
from rbac.service.init_permission import init_permission


def login(request):

    if request.method == 'GET':
        return render(request, 'login.html')

    username = request.POST.get('user')
    pwd = get_md5(request.POST.get('pwd'))

    user = models.UserInfo.objects.filter(name=username, password=pwd).first()
    
    if not user:
        return render(request, 'login.html', {'msg': '用户名或密码错误!'})
    request.session['user_info'] = {'id': user.id, 'nickname': user.nickname}

    init_permission(request, user)
    return redirect('/index/')


def logout(request):

    request.session.flush()
    return redirect('/login/')


def index(request):
    return render(request, 'index.html')


























