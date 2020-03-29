# -*- coding: utf-8 -*-
# @Time    : 2019/11/14  22:14
# @Author  : XiaTian
# @File    : role.py

from django.shortcuts import render, HttpResponse, redirect
from rbac.forms.role import RoleModelForm


from rbac import models
from rbac.service import urls


def  role_list(request):

    roles = models.Role.objects.all()

    return render(request, 'rbac/role_list.html', {'roles': roles})


def role_add(request):

    if request.method == 'GET':
        form = RoleModelForm()

        return render(request, 'rbac/change.html', {'form': form})

    form = RoleModelForm(request.POST)
    if form.is_valid():

        form.save()

        return redirect(urls.memory_reverse(request, 'rbac:role_list'))

    return render(request, 'rbac/change.html', {'form': form})


def role_edit(request, pk):
    
    role_obj = models.Role.objects.filter(pk=pk).first()

    if not role_obj:
        return HttpResponse('请先选择角色，再操作!')

    if request.method == 'GET':
        form = RoleModelForm(instance=role_obj)

        return render(request, 'rbac/change.html', {'form': form})
    form = RoleModelForm(instance=role_obj, data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(urls.memory_reverse(request, 'rbac:role_list'))
    return render(request, 'rbac/change.html', {'form': form})


def role_del(request, pk):
    url = urls.memory_reverse(request, 'rbac:role_list')
    if request.method == 'GET':
        return render(request, 'rbac/delete.html', {'cancel': url})
    models.Role.objects.filter(pk=pk).delete()

    return redirect(url)