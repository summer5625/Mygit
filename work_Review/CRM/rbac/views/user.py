# -*- coding: utf-8 -*-
# @Time    : 2019/10/27  16:38
# @Author  : XiaTian
# @File    : user.py


from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse

from rbac import models
from rbac.forms import user


def user_list(request):
    '''
    角色信息展示视图
    :param request:
    :return:
    '''

    user_queryset = models.UserInfo.objects.all()

    return render(request, 'rbac/user_list.html', {'users': user_queryset})


def user_add(request):
    '''
    添加新角色视图
    :param request:
    :return:
    '''
    if request.method == 'GET':
        form = user.UserModelForm()

        return render(request, 'rbac/role_change.html', {'form': form})

    form = user.UserModelForm(request.POST)

    if form.is_valid():
        form.save()

        return redirect(reverse('rbac:user_list'))

    return render(request, 'rbac/role_change.html', {'form': form})


def user_edit(request, pk):
    '''
    修改角色信息视图
    :param request:
    :param pk:
    :return:
    '''

    role_obj = models.UserInfo.objects.filter(pk=pk).first()

    if not role_obj:
        return HttpResponse('角色不存在!')

    if request.method == 'GET':
        form = user.UpdateUserModelForm(instance=role_obj)  # 修改信息时，如果给form组件加上一个实例化数据库的对象，在页面上就会自动默认显示该对象对应的字段值

        return render(request, 'rbac/role_change.html', {'form': form})

    # 用户提交修改后的数据，参数instance是指明要修改数据库的那条数据，data是用户提交的修改字段信息
    form = user.UpdateUserModelForm(instance=role_obj, data=request.POST)

    if form.is_valid():
        form.save()

        return redirect(reverse('rbac:user_list'))

    return render(request, 'rbac/role_change.html', {'form': form})


def user_del(request, pk):
    '''
    删除角色信息
    :param request:
    :param pk:
    :return:
    '''
    
    if request.method == 'GET':
        return render(request, 'rbac/delete.html', {'cancel': reverse('rbac:user_list')})

    models.UserInfo.objects.filter(pk=pk).delete()

    return redirect(reverse('rbac:user_list'))


def user_reset_pwd(request, pk):
    '''
    密码重置
    :param request: 
    :param pk: 
    :return: 
    '''
    
    user_obj = models.UserInfo.objects.filter(pk=pk).first()
    if not user_obj:
        return HttpResponse('用户不存在!')
    
    if request.method == 'GET':
        form = user.ResetPasswordUserModelForm()
        
        return render(request, 'rbac/role_change.html', {'form': form})
    
    form = user.ResetPasswordUserModelForm(instance=user_obj, data=request.POST)
    
    if form.is_valid():
        
        form.save()
        
        return redirect(reverse('rbac:user_list'))

    return render(request, 'rbac/role_change.html', {'form': form})