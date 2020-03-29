# -*- coding: utf-8 -*-
# @Time    : 2019/11/1  18:12
# @Author  : XiaTian
# @File    : account.py


from django.shortcuts import render, redirect


from web import models
from web.utils.md5 import get_md5
from rbac.service.init_permission import init_permission


def login(request):
    '''
    用户认证视图
    :param request:
    :return:
    '''
    if request.method == 'GET':
        return render(request, 'login.html')

    username = request.POST.get('user')
    pwd = get_md5(request.POST.get('pwd'))

    user = models.UserInfo.objects.filter(name=username, password=pwd).first()

    if not user:
        return render(request, 'login.html', {'msg': '用户名或密码错误'})

    request.session['user_info'] = {'id': user.id, 'nickname': user.nickname}
    
    # # 初始化用户权限
    init_permission(request, user)

    return redirect('/index/')


def logout(request):
    '''
    注销视图
    :param request:
    :return:
    '''
    request.session.flush()

    return redirect('/login/')


def index(request):

    return render(request, 'index.html')