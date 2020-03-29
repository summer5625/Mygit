# -*- coding: utf-8 -*-
# @Time    : 2019/11/14  22:15
# @Author  : XiaTian
# @File    : menu.py

from collections import OrderedDict
from django.shortcuts import render, HttpResponse, redirect
from django.forms import formset_factory

from rbac import models
from rbac.forms.menu import MenuModelForm, SecondMenuModelForm, PermissionModelForm
from rbac.forms.menu import MultiUpdatePermissionsForm, MultiAddPermissionsForm
from rbac.service import routes
from rbac.service import urls


def menu_list(request):
    menus = models.Menu.objects.all()
    menu_id = request.GET.get('mu')
    second_mu_id = request.GET.get('sid')

    if menu_id:
        second_menu = models.Permission.objects.filter(menu_id=menu_id)
    else:
        second_menu = []

    if second_mu_id:
        permissions = models.Permission.objects.filter(pid_id=second_mu_id)
    else:
        permissions = []

    return render(request, 'rbac/menu_list.html',
                  {'menus': menus, 'menu_id': menu_id, 'second_menu': second_menu, 'second_menu_id': second_mu_id,
                   'permissions': permissions})


def menu_add(request):
    if request.method == 'GET':
        form = MenuModelForm()

        return render(request, 'rbac/change.html', {'form': form})

    form = MenuModelForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect(urls.memory_reverse(request, 'rbac:menu_list'))

    return render(request, 'rbac/change.html', {'form': form})


def menu_edit(request, pk):
    menu_obj = models.Menu.objects.filter(pk=pk).first()
    if not menu_obj:
        return HttpResponse('选择菜单不存在!')

    if request.method == 'GET':
        form = MenuModelForm(instance=menu_obj)

        return render(request, 'rbac/change.html', {'form': form})

    form = MenuModelForm(instance=menu_obj, data=request.POST)

    if form.is_valid():
        form.save()
        return redirect(urls.memory_reverse(request, 'rbac:menu_list'))

    return render(request, 'rbac/change.html', {'form': form})


def menu_del(request, pk):
    url = urls.memory_reverse(request, 'rbac:menu_list')
    if request.method == 'GET':
        return render(request, 'rbac/delete.html', {'cancel': url})

    models.Menu.objects.filter(pk=pk).delete()

    return redirect(url)


def second_menu_add(request, menu_id):

    menu_obj = models.Menu.objects.filter(pk=menu_id).first()
    
    if request.method == 'GET':

        form = SecondMenuModelForm(initial={'menu': menu_obj})
        return render(request, 'rbac/change.html', {'form': form})
    form = SecondMenuModelForm(request.POST)
    
    if form.is_valid():
        
        form.save()
        return redirect(urls.memory_reverse(request, 'rbac:menu_list'))
    return render(request, 'rbac/change.html', {'form': form})


def second_menu_edit(request, pk):

    second_menu = models.Permission.objects.filter(pk=pk).first()

    if not second_menu:
        return HttpResponse('菜单不存在!')
    if request.method == 'GET':
        form = SecondMenuModelForm(instance=second_menu)
        return render(request, 'rbac/change.html', {'form': form})
    form = SecondMenuModelForm(instance=second_menu, data=request.POST)

    if form.is_valid():

        form.save()
        return redirect(urls.memory_reverse(request, 'rbac:menu_list'))
    return render(request, 'rbac/change.html', {'form': form})


def second_menu_del(request, pk):
    url = urls.memory_reverse(request, 'rbac:menu_list')
    if request.method == 'GET':

        return render(request, 'rbac/delete.html', {'cancel': url})

    models.Permission.objects.filter(pk=pk).delete()
    
    return redirect(url)


def permission_add(request, second_menu_id):

    if request.method == 'GET':
        form = PermissionModelForm()
        return render(request, 'rbac/change.html', {'form': form})
    form = PermissionModelForm(request.POST)

    if form.is_valid():

        second_menu_obj = models.Permission.objects.filter(pk=second_menu_id).first()
        if not second_menu_obj:
            return HttpResponse('二级菜单不存在!')
        form.instance.pid = second_menu_obj
        form.save()
        return redirect(urls.memory_reverse(request, 'rbac:menu_list'))
    return render(request, 'rbac/change.html', {'form': form})


def permission_edit(request, pk):
    permission_obj = models.Permission.objects.filter(pk=pk).first()

    if not permission_obj:
        return HttpResponse('权限不存在!')

    if request.method == 'GET':
        form = PermissionModelForm(instance=permission_obj)

        return render(request, 'rbac/change.html', {'form': form})

    form = PermissionModelForm(instance=permission_obj, data=request.POST)

    if form.is_valid():
        form.save()

        return redirect(urls.memory_reverse(request, 'rbac:menu_list'))

    return render(request, 'rbac/change.html', {'form': form})


def permission_del(request, pk):
    
    url = urls.memory_reverse(request, 'rbac:menu_list')

    if request.method == 'GET':

        return render(request, 'rbac/delete.html', {'cancel': url})

    models.Permission.objects.filter(pk=pk).delete()

    return redirect(url)


def multi_permission(request):
    
    post_type = request.GET.get('type')

    formset_add_class = formset_factory(MultiAddPermissionsForm, extra=0)
    update_formset_class = formset_factory(MultiUpdatePermissionsForm, extra=0)
    generate_formset = None
    update_formset = None

    # 添加url
    if request.method == 'POST' and post_type == 'generate':

        formset = formset_add_class(request.POST)
        if formset.is_valid():
            post_row_list = formset.cleaned_data
            obj_list = []
            has_error = False
            for i in range(0, formset.total_form_count()):
                row = post_row_list[i]

                try:
                    obj = models.Permission(**row)
                    obj.validate_unique() # 判断唯一性
                    obj_list.append(obj)
                except Exception as e:
                    formset.errors[i].update(e)
                    generate_formset = formset
                    has_error = True
            if not has_error:
                models.Permission.objects.bulk_create(obj_list, batch_size=50)
        else:
            generate_formset = formset

    # 更新url
    if request.method == 'POST' and post_type == 'update':
        formset = update_formset_class(request.POST)

        if formset.is_valid():
            post_update_list = formset.cleaned_data

            for i in range(0, formset.total_form_count()):
                update_row = post_update_list[i]
                print(update_row)
                permission_id = update_row.pop('id')

                try:
                    update_obj = models.Permission.objects.filter(id=permission_id).first()

                    for k, v in update_row.items():
                        setattr(update_obj, k, v)

                    update_obj.validate_unique()
                    update_obj.save()
                except Exception as e:
                    formset.errors[i].update(e)
                    update_formset = formset
        else:
            update_formset = formset

    # 获得程序和数据库中的url
    auto_get_all_url = routes.get_all_url_dict()
    routes_name_set = set(auto_get_all_url.keys())

    permission_list = models.Permission.objects.all().values('id', 'title', 'url', 'name', 'menu_id', 'pid_id')
    permission_dict = OrderedDict()

    for item in permission_list:

        permission_dict[item['name']] = item

    permission_set = set(permission_dict.keys())

    for name, value in permission_dict.items():
        
        router_row_dict = auto_get_all_url.get(name)

        if not router_row_dict:
            continue
        
        if value['url'] != router_row_dict['url']:
            value['url'] = '路由和数据库中不一致!'

    # 待增加的url
    if not generate_formset:

        generate_name_list = routes_name_set - permission_set
        generate_formset = formset_add_class(
            initial=[row_dict for name, row_dict in auto_get_all_url.items() if name in generate_name_list])
    
    # 待删除url
    delete_name_list = permission_set - routes_name_set
    delete_row_list = [row_dict for name, row_dict in permission_dict.items() if name in delete_name_list]

    # 待更新url
    if not update_formset:

        update_name_list = permission_set & routes_name_set
        update_formset = update_formset_class(
            initial=[row_dict for name, row_dict in permission_dict.items() if name in update_name_list])
        
    return render(request, 'rbac/multi_permission.html', {
        'generate_formset': generate_formset,
        'delete_row_list': delete_row_list,
        'update_formset': update_formset
    })


def multi_permission_del(request, pk):
    
    url = urls.memory_reverse(request, 'rbac:multi_permission')

    if request.method == 'GET':

        return render(request, 'rbac/delete.html', {'cancel': url})

    models.Permission.objects.filter(pk=pk).delete()

    return redirect(url)


def distribute_permission(request):

    role_id = request.GET.get('rid')
    user_id = request.GET.get('uid')
    role_obj = models.Role.objects.filter(pk=role_id).first()
    user_obj = models.UserInfo.objects.filter(pk=user_id).first()
    if not role_obj:
        role_id = None
    if not user_obj:
        user_id = None

    # 修改用户角色
    if request.method == 'POST' and request.POST.get('type') == 'role':
        change_role_list = request.POST.getlist('role')

        if not user_obj:
            return HttpResponse('请先选择用户，再分配角色!')

        user_obj.roles.set(change_role_list)

    # 修改角色权限
    if request.method == 'POST' and request.POST.get('type') == 'permission':

        change_permission_list = request.POST.getlist('permissions')

        if not role_obj:
            return HttpResponse('请先选择角色，再分配权限!')

        role_obj.permissions.set(change_permission_list)
        
    # 获取权限信息
    if role_obj:
        user_permission = role_obj.permissions.all()
        user_permission_dict = {item.id: None for item in user_permission}

    elif user_obj:
        user_permission = user_obj.roles.values('permissions').filter(permissions__id__isnull=False).distinct()
        user_permission_dict = {item['permissions']: None for item in user_permission}
    else:
        user_permission_dict = {}

    # 获取用户信息
    if user_id:
        user_role = user_obj.roles.all()
    else:
        user_role = []
    user_role_dict = {item.id: None for item in user_role}

    # 所有的用户和角色
    all_user_list = models.UserInfo.objects.all()
    all_role_list = models.Role.objects.all()

    # 所有的一级菜单
    all_menu_list = models.Menu.objects.all().values('id', 'title')
    all_menu_dict = {}
    
    for item in all_menu_list:
        all_menu_dict[item['id']] = item
        all_menu_dict[item['id']]['children'] = []

    # 所有的二级菜单
    all_second_menu_list = models.Permission.objects.filter(menu__isnull=False).values('id', 'title', 'menu_id')
    all_second_menu_dict = {}

    for item in all_second_menu_list:
        all_second_menu_dict[item['id']] = item
        all_second_menu_dict[item['id']]['children'] = []

        mid = item['menu_id']
        if mid in all_menu_dict:
            all_menu_dict[mid]['children'].append(item)

    # 所有的三级菜单
    all_permission_list = models.Permission.objects.filter(menu__isnull=True).values('id', 'title', 'pid_id')

    for item in all_permission_list:

        pk = item['pid_id']
        if pk not in all_second_menu_dict:
            continue

        all_second_menu_dict[pk]['children'].append(item)

    return render(request, 'rbac/distribute_permission.html', {
        'user_list': all_user_list,
        'role_id': role_id,
        'role_list': all_role_list,
        'all_menu_list': all_menu_list,
        'user_id': user_id,
        'user_role_dict': user_role_dict,
        'user_permission_dict': user_permission_dict,
    })

        

























