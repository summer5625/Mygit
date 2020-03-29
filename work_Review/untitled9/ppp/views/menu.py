# -*- coding: utf-8 -*-
# @Time    : 2020/1/29  16:17
# @Author  : XiaTian
# @File    : menu.py
from collections import OrderedDict
from django.shortcuts import reverse, render, redirect, HttpResponse
from django.forms import formset_factory
from ppp import models
from ppp.forms import menu
from ppp.service import routes


# #######################################一级菜单########################################
def menu_list(request):
    menus = models.Menu.objects.all()
    mid = request.GET.get('menu')
    second_menu_id = request.GET.get('sid')

    if mid:
        second_menu = models.Permission.objects.filter(menu_id=mid)
    else:
        second_menu = []
    if second_menu_id:
        permissions = models.Permission.objects.filter(p_id=second_menu_id)
    else:
        permissions = []

    return render(request, 'menu_list.html',
                  {'menus': menus, 'menu_id': mid, 'second_menu': second_menu, 'second_menu_id': second_menu_id,
                   'permissions': permissions})


def menu_add(request):

    if request.method == 'GET':
        form = menu.MenuModelForm()
        return render(request, 'change.html', {'form': form})

    form = menu.MenuModelForm(request.POST)
    
    if form.is_valid():
        form.save()
        return redirect(reverse('ppp:menu_list'))
    return render(request, 'change.html', {'form': form})


def menu_edit(request, pk):

    menu_obj = models.Menu.objects.filter(pk=pk).first()

    if not menu_obj:
        return HttpResponse('菜单不存在')
    if request.method == 'GET':
        form = menu.MenuModelForm(instance=menu_obj)
        
        return render(request, 'change.html', {'form': form})
    
    form = menu.MenuModelForm(instance=menu_obj, data=request.POST)

    if form.is_valid():
        form.save()
        return redirect(reverse('ppp:menu_list'))
    return render(request, 'change.html', {'form': form})


def menu_del(request, pk):
    
    if request.method == 'GET':
        return render(request, 'delete.html', {'cancel': reverse('ppp:menu_list')})
    
    models.Menu.objects.filter(pk=pk).delete()
    return redirect(reverse('ppp:menu_list'))


# #######################################二级菜单########################################
def second_menu_add(request, menu_id):

    menu_obj = models.Menu.objects.filter(pk=menu_id).first()
    if request.method == 'GET':
        form = menu.SecondMenu(initial={'menu': menu_obj})
        return render(request, 'change.html', {'form': form})
    form = menu.SecondMenu(request.POST)
    
    if form.is_valid():
        form.save()
        return redirect(reverse('ppp:menu_list'))
    return render(request, 'change.html', {'form': form})
        

def second_menu_edit(request, pk):

    permission_obj = models.Permission.objects.filter(pk=pk).first()

    if not permission_obj:
        return HttpResponse('菜单不存在')
    if request.method == 'GET':
        form = menu.SecondMenu(instance=permission_obj)
        return render(request, 'change.html', {'form': form})
    form = menu.SecondMenu(instance=permission_obj, data=request.POST)

    if form.is_valid():
        form.save()
        return redirect(reverse('ppp:menu_list'))
    return render(request, 'change.html', {'form': form})


def second_menu_del(request, pk):
    
    if request.method == 'GET':
        return render(request, 'delete.html', {'cancel': reverse('ppp:menu_list')})

    models.Permission.objects.filter(id=pk).delete()
    return redirect(reverse('ppp:menu_list'))


# #######################################三级菜单########################################
def permission_add(request, second_menu_id):

    if request.method == 'GET':
        form = menu.PermissionModel()
        return render(request, 'change.html', {'form': form})

    form = menu.PermissionModel(request.POST)

    if form.is_valid():
        second_menu_obj = models.Permission.objects.filter(id=second_menu_id).first()
        if not second_menu_obj:
            return HttpResponse('菜单不存在')

        form.instance.p_id = second_menu_obj
        form.save()
        return redirect(reverse('ppp:menu_list'))

    return render(request, 'change.html', {'form': form})


def permission_edit(request, pk):

    permission_obj = models.Permission.objects.filter(pk=pk).first()

    if not permission_obj:
        return HttpResponse('菜单不存在')
    if request.method == 'GET':
        form = menu.PermissionModel(instance=permission_obj)
        return render(request, 'change.html', {'form': form})
    
    form = menu.PermissionModel(instance=permission_obj, data=request.POST)

    if form.is_valid():
        form.save()
        return redirect(reverse('ppp:menu_list'))
    return render(request, 'change.html', {'form': form})


def permission_del(request, pk):
    
    if request.method == 'GET':
        return render(request, 'delete.html', {'cancel': reverse('ppp:menu_list')})

    models.Permission.objects.filter(pk=pk).delete()
    return redirect(reverse('ppp:menu_list'))


# #######################################权限管理########################################
def multi_permission(request):
    
    post_type = request.GET.get('type')
    formset_add_class = formset_factory(menu.MultiAddPermission, extra=0)
    generate_formset = None
    print(post_type)
    # 批量增加权限
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
                    obj.validate_unique()
                    obj_list.append(obj)
                except Exception as e:
                    formset.errors[i].update(e)
                    generate_formset = formset
                    has_error = True

            if not has_error:
                models.Permission.objects.bulk_create(obj_list, batch_size=50)
        else:
            generate_formset = formset

    # 批量更新权限
    update_formset_class = formset_factory(menu.MultiUpdatePermission, extra=0)
    update_formset = None
    
    if request.method == 'POST' and post_type == 'update':
        formset = update_formset_class(request.POST)
        if formset.is_valid():
            post_update_list = formset.cleaned_data
            for i in range(0, formset.total_form_count()):
                update_row = post_update_list[i]
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

    # 自动发现项目中的url
    auto_get_all_url = routes.get_all_url_dict()
    router_name_set = set(auto_get_all_url.keys()) # 去重
    
    # 获取数据库中所有url
    permission_list = models.Permission.objects.all().values('id', 'title', 'name', 'url', 'menu_id', 'p_id_id')
    permission_dict = OrderedDict()

    for row in permission_list:

        permission_dict[row['name']] = row
    permission_name_set = set(permission_dict.keys())

    for name, value in permission_dict.items():
        route_row_dict = auto_get_all_url.get(name)
        
        if not route_row_dict:
            continue
        if value['url'] != route_row_dict['url']:
            value['url'] = '路由和数据库不一致'

    # 获取待操作权限
    if not generate_formset:
        generate_name_list = router_name_set - permission_name_set
        generate_formset = formset_add_class(
            initial=[row_dict for name, row_dict in auto_get_all_url.items() if name in generate_name_list])
    
    # 待删除权限
    delete_name_list = permission_name_set - router_name_set
    delete_row_list = [row_dict for name, row_dict in  permission_dict.items() if name in delete_name_list]

    # 待更新
    if not update_formset:
        update_name_list = router_name_set & permission_name_set
        update_formset = update_formset_class(
            initial=[row_dict for name, row_dict in permission_dict.items() if name in update_name_list])

    return render(request, 'multi_permission.html', {
        'generate_formset': generate_formset,
        'delete_row_list': delete_row_list,
        'update_formset': update_formset})


def multi_permission_del(request, pk):

    if request.method == 'GET':
        return render(request, 'delete.html', {'cancel': reverse('ppp:multi_permission')})
    
    models.Permission.objects.filter(pk=pk).delete()
    return redirect(reverse('ppp:multi_permission'))


def distribute_permission(request):

    role_id = request.GET.get('rid')
    user_id = request.GET.get('uid')
    role_obj = models.Role.objects.filter(pk=role_id).first()
    user_obj = models.UserInfo.objects.filter(pk=user_id).first()
    if not role_obj:
        role_id = None
    if not user_obj:
        user_id = None

    if request.method == 'POST' and request.POST.get('type') == 'role':
        change_role_list = request.POST.getlist('role')
        if not user_obj:
            return HttpResponse('请先选择用户，再分配角色!')
        user_obj.roles.set(change_role_list) # 给用户绑定角色

    if request.method == 'POST' and request.POST.get('type') == 'permission':
        change_permission_list = request.POST.getlist('permissions')
        if not role_obj:
            return HttpResponse('请先选择角色，再分配权限!')

        role_obj.permissions.set(change_permission_list)

    if role_obj:
        user_permission = role_obj.permissions.all()
        user_permission_dict = {item.id: None for item in user_permission}
    elif user_obj:
        user_permission = user_obj.roles.values('permissions').filter(permissions__id__isnull=False).distinct()
        user_permission_dict = {item['permissions']: None for item in user_permission}
    else:
        user_permission_dict = {}
    
    if user_id:
        user_role = user_obj.roles.all()
    else:
        user_role = []
    user_role_dict = {item.id: None for item in user_role}

    all_user_list = models.UserInfo.objects.all()
    all_role_list = models.Role.objects.all()

    all_menu_list = models.Menu.objects.all().values('id', 'title')
    all_menu_dict = {}

    for item in all_menu_list:
        item['children'] = []
        all_menu_dict[item['id']] = item

    all_second_menu_list = models.Permission.objects.filter(menu__isnull=False).values('id', 'title', 'menu_id')
    all_second_menu_dict = {}
    for item in all_second_menu_list:
        item['children'] = []
        all_second_menu_dict[item['id']] = item
        mid = item['menu_id']
        if mid in all_menu_dict:
            all_menu_dict[mid]['children'].append(item)

    all_permission_list = models.Permission.objects.filter(menu__isnull=True).values('id', 'title', 'p_id')
    
    for row in all_permission_list:
        pid = row['p_id']
        if pid not in all_second_menu_dict:
            continue
        all_second_menu_dict[pid]['children'].append(row)
 
    return render(request, 'distribute_permission.html', {
        'user_list': all_user_list,
        'role_id': role_id,
        'role_list': all_role_list,
        'all_menu_list': all_menu_list,
        'user_id': user_id,
        'user_role_dict': user_role_dict,
        'user_permission_dict': user_permission_dict
    })























































