# -*- coding: utf-8 -*-
# @Time    : 2020/1/29  16:16
# @Author  : XiaTian
# @File    : role.py
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from ppp import models
from ppp.forms import role


def role_list(request):
    
    role_queryset = models.Role.objects.all()

    return render(request, 'role_list.html', {'roles': role_queryset})


def role_add(request):
    
    if request.method == 'GET':
        form = role.RoleModelForm()
        render(request, 'change.html', {'form': form})
    
    form = role.RoleModelForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('ppp:role_list'))
    return render(request, 'change.html', {'form': form})


def role_edit(request, pk):
    
    role_obj = models.Role.objects.filter(pk=pk).first()
    
    if not role_obj:
        return HttpResponse('角色不存在')
    
    if request.method == 'GET':
        
        form = role.RoleModelForm(instance=role_obj)
        return render(request, 'change.html', {'form': form})
    
    form = role.RoleModelForm(instance=role_obj, data=request.POST)

    if form.is_valid():
        form.save()
        return redirect(reverse('ppp:role_list'))
    return render(request, 'change.html', {'form': form})


def role_del(request, pk):

    if request.method == 'GET':
        return render(request, 'delete.html', {'cancel': reverse('ppp:role_list')})
    
    models.Role.objects.filter(pk=pk).delete()
    return redirect(reverse('ppp:role_list'))



















