# -*- coding: utf-8 -*-
# @Time    : 2019/11/14  22:15
# @Author  : XiaTian
# @File    : user.py

from django.shortcuts import render, HttpResponse, redirect
from rbac.forms.user import UpdateUserInfoModelForm, UserInfoModelForm, ResetPasswordUserModelForm


from rbac import models
from rbac.service import urls


def user_list(request):
    
    users = models.UserInfo.objects.all()
    
    return render(request, 'rbac/user_list.html', {'users': users})


def user_add(request):
    
    if request.method =='GET':
        
        form = UserInfoModelForm()
        return render(request, 'rbac/change.html', {'form': form})
    
    form = UserInfoModelForm(request.POST)
    
    if form.is_valid():
        form.save()
        
        return redirect(urls.memory_reverse(request, 'rbac:user_list'))
    
    return render(request, 'rbac/change.html', {'form': form})


def user_edit(request, pk):

    user_obj = models.UserInfo.objects.filter(pk=pk).first()

    if not user_obj:
        return HttpResponse('请先选择用户，再操作!')

    if request.method == 'GET':
        form = UpdateUserInfoModelForm(instance=user_obj)

        return render(request, 'rbac/change.html', {'form': form})
    form = UpdateUserInfoModelForm(instance=user_obj, data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(urls.memory_reverse(request, 'rbac:user_list'))
    return render(request, 'rbac/change.html', {'form': form})


def user_del(request, pk):
    url = urls.memory_reverse(request, 'rbac:user_list')
    if request.method == 'GET':

        return render(request, 'rbac/delete.html', {'cancel': url})
    models.UserInfo.objects.filter(pk=pk).delete()

    return redirect(url)


def reset_password(request, pk):
    
    user_obj = models.UserInfo.objects.filter(pk=pk).first()

    if not user_obj:
        return HttpResponse('请先选择用户，再操作!')
    
    if request.method == 'GET':
        form = ResetPasswordUserModelForm()
        
        return render(request, 'rbac/change.html', {'form': form})
    form = ResetPasswordUserModelForm(instance=user_obj, data=request.POST)

    if form.is_valid():
        form.save()

        return redirect(urls.memory_reverse(request, 'rbac:user_list'))
    return render(request, 'rbac/change.html', {'form': form})