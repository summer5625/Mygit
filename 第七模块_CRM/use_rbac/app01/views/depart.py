# -*- coding: utf-8 -*-
# @Time    : 2019/11/1  22:29
# @Author  : XiaTian
# @File    : depart.py

from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse


from app01 import models
from app01.forms import depart
from rbac.service.urls import memory_reverse


def depart_list(request):
    '''
    主机信息展示视图
    :param request:
    :return:
    '''

    depart_queryset = models.Department.objects.all()

    return render(request, 'depart_list.html', {'departs':  depart_queryset})


def depart_add(request):
    '''
    添加新主机视图
    :param request:
    :return:
    '''
    if request.method == 'GET':
        form = depart.DepartmentModelForm()

        return render(request, 'rbac/role_change.html', {'form': form})

    form = depart.DepartmentModelForm(request.POST)

    if form.is_valid():
        form.save()

        return redirect(memory_reverse(request, 'depart_list'))

    return render(request, 'rbac/role_change.html', {'form': form})


def depart_edit(request, pk):
    '''
    修改主机
    :param request:
    :param pk:
    :return:
    '''

    depart_obj = models.Department.objects.filter(pk=pk).first()

    if not depart_obj:
        return HttpResponse('主机不存在!')

    if request.method == 'GET':
        form = depart.DepartmentModelForm(instance=depart_obj)

        return render(request, 'rbac/role_change.html', {'form': form})

    # 用户提交修改后的数据，参数instance是指明要修改数据库的那条数据，data是用户提交的修改字段信息
    form = depart.DepartmentModelForm(instance=depart_obj, data=request.POST)

    if form.is_valid():
        form.save()

        return redirect(memory_reverse(request, 'depart_list'))

    return render(request, 'rbac/role_change.html', {'form': form})


def depart_del(request, pk):
    '''
    删除主机
    :param request:
    :param pk:
    :return:
    '''

    if request.method == 'GET':
        return render(request, 'rbac/delete.html', {'cancel': reverse('depart_list')})

    models.Department.objects.filter(pk=pk).delete()

    return redirect(memory_reverse(request, 'depart_list'))
