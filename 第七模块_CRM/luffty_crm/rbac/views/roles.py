# -*- coding: utf-8 -*-
# @Time    : 2019/10/26  19:10
# @Author  : XiaTian
# @File    : roles.py


from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse

from rbac import models
from rbac.forms import role


def role_list(request):
    '''
    角色信息展示视图
    :param request:
    :return:
    '''

    role_queryset = models.Role.objects.all()

    return render(request, 'rbac/role_list.html', {'roles': role_queryset})


def role_add(request):
    '''
    添加新角色视图
    :param request:
    :return:
    '''
    if request.method == 'GET':

        form = role.RoleModelForm()

        return render(request, 'rbac/role_change.html', {'form': form})

    form = role.RoleModelForm(request.POST)

    if form.is_valid():

        form.save()

        return redirect(reverse('rbac:role_list'))

    return render(request, 'rbac/role_change.html', {'form': form})


def role_edit(request, pk):
    '''
    修改角色信息视图
    :param request:
    :param pk:
    :return:
    '''

    role_obj = models.Role.objects.filter(pk=pk).first()

    if not role_obj:

        return HttpResponse('角色不存在!')
    
    if request.method == 'GET':
        
        form = role.RoleModelForm(instance=role_obj) # 修改信息时，如果给form组件加上一个实例化数据库的对象，在页面上就会自动默认显示该对象对应的字段值

        return render(request, 'rbac/role_change.html', {'form': form})

    # 用户提交修改后的数据，参数instance是指明要修改数据库的那条数据，data是用户提交的修改字段信息
    form = role.RoleModelForm(instance=role_obj, data=request.POST)
    
    if form.is_valid():
        
        form.save()

        return redirect(reverse('rbac:role_list'))
        
    return render(request, 'rbac/role_change.html', {'form': form})


def role_del(request, pk):
    '''
    删除角色信息
    :param request: 
    :param pk: 
    :return: 
    '''

    if request.method == 'GET':

        return render(request, 'rbac/delete.html', {'cancel': reverse('rbac:role_list')})
    
    models.Role.objects.filter(pk=pk).delete()

    return redirect(reverse('rbac:role_list'))