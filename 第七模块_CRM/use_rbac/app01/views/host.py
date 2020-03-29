# -*- coding: utf-8 -*-
# @Time    : 2019/11/1  21:56
# @Author  : XiaTian
# @File    : host.py

from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse


from app01 import models
from app01.forms import host
from rbac.service.urls import memory_reverse


def host_list(request):
    '''
    主机信息展示视图
    :param request:
    :return:
    '''

    host_queryset = models.Host.objects.all()

    return render(request, 'host_list.html', {'hosts': host_queryset})
    

def host_add(request):
    '''
    添加新主机视图
    :param request:
    :return:
    '''
    if request.method == 'GET':
        form = host.HostModelForm()

        return render(request, 'rbac/role_change.html', {'form': form})

    form = host.HostModelForm(request.POST)

    if form.is_valid():
        form.save()

        return redirect(memory_reverse(request, 'host_list'))

    return render(request, 'rbac/role_change.html', {'form': form})


def host_edit(request, pk):
    '''
    修改主机
    :param request:
    :param pk:
    :return:
    '''

    host_obj = models.Host.objects.filter(pk=pk).first()

    if not host_obj:
        return HttpResponse('主机不存在!')

    if request.method == 'GET':
        form = host.HostModelForm(instance=host_obj)

        return render(request, 'rbac/role_change.html', {'form': form})

    # 用户提交修改后的数据，参数instance是指明要修改数据库的那条数据，data是用户提交的修改字段信息
    form = host.HostModelForm(instance=host_obj, data=request.POST)

    if form.is_valid():
        form.save()

        return redirect(memory_reverse(request, 'host_list'))

    return render(request, 'rbac/role_change.html', {'form': form})


def host_del(request, pk):
    '''
    删除主机
    :param request:
    :param pk:
    :return:
    '''

    if request.method == 'GET':
        return render(request, 'rbac/delete.html', {'cancel': reverse('host_list')})

    models.Host.objects.filter(pk=pk).delete()

    return redirect(memory_reverse(request, 'host_list'))
    
    