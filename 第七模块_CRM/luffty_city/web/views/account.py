from django.shortcuts import render, redirect

from rbac import models
from rbac.service.init_permission import init_permission


def login(request):
    '''
    用户认证视图
    :param request:
    :return:
    '''
    if request.method == 'GET':
        return render(request, 'login.html')

    user = request.POST.get('user')
    pwd = request.POST.get('pwd')

    current_user = models.UserInfo.objects.filter(name=user, password=pwd).first()

    if not current_user:
        return render(request, 'login.html', {'msg': '用户名或密码错误'})

    # 初始化用户权限
    init_permission(request, current_user)

    return redirect('/customer/list/')


def logout(request):
    '''
    注销视图
    :param request: 
    :return: 
    '''
    request.session.flush()
    
    return redirect('/login/')