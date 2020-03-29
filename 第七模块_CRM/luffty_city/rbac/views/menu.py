# -*- coding: utf-8 -*-
# @Time    : 2019/10/28  11:30
# @Author  : XiaTian
# @File    : menu.py

from collections import OrderedDict
from django.shortcuts import render, HttpResponse, redirect
from django.forms import formset_factory

from rbac import models
from rbac.forms import menu
from rbac.service import urls
from rbac.service import routes


def menu_list(request):
    '''
    菜单类别展示
    :param request:
    :return:
    '''
    menus = models.Menu.objects.all()  # 一级菜单列表

    mid = request.GET.get('menu')  # 用户选择的一级菜单id
    second_menu_id = request.GET.get('sid')  # 用户选择的二级菜单id

    if mid:
        second_menu = models.Permission.objects.filter(menu_id=mid)  # 二级菜单列表
    else:
        second_menu = []

    if second_menu_id:
        permissions = models.Permission.objects.filter(
            p_id=second_menu_id)  # 权限表
    else:
        permissions = []

    return render(request,
                  'rbac/menu_list.html',
                  {'menus': menus,
                   'menu_id': mid,
                   'second_menu': second_menu,
                   'second_menu_id': second_menu_id,
                   'permissions': permissions})


def menu_add(request):
    '''
    新增一级菜单
    :param request:
    :return:
    '''
    if request.method == 'GET':
        form = menu.MenuModelForm()

        return render(request, 'rbac/role_change.html', {'form': form})

    form = menu.MenuModelForm(request.POST)

    if form.is_valid():
        form.save()

        return redirect(urls.memory_reverse(request, 'rbac:menu_list'))

    return render(request, 'rbac/role_change.html', {'form': form})


def menu_edit(request, pk):
    '''
    编辑一级菜单
    :param request:
    :param pk:
    :return:
    '''
    menu_obj = models.Menu.objects.filter(pk=pk).first()

    if not menu_obj:
        return HttpResponse('角色不存在!')

    if request.method == 'GET':
        form = menu.MenuModelForm(instance=menu_obj)

        return render(request, 'rbac/role_change.html', {'form': form})

    form = menu.MenuModelForm(instance=menu_obj, data=request.POST)

    if form.is_valid():
        form.save()

        return redirect(urls.memory_reverse(request, 'rbac:menu_list'))

    return render(request, 'rbac/role_change.html', {'form': form})


def menu_del(request, pk):
    '''
    删除一级菜单
    :param request:
    :param pk:
    :return:
    '''
    url = urls.memory_reverse(request, 'rbac:menu_list')
    if request.method == 'GET':
        return render(request, 'rbac/delete.html', {'cancel': url})

    models.Menu.objects.filter(pk=pk).delete()

    return redirect(url)


def second_menu_add(request, menu_id):
    '''
    新增二级菜单
    :param request:
    :param menu_id:
    :return:
    '''
    menu_obj = models.Menu.objects.filter(mid=menu_id).first()

    if request.method == 'GET':
        form = menu.SecondMenuModelForm(initial={'menu': menu_obj})

        return render(request, 'rbac/role_change.html', {'form': form})

    form = menu.SecondMenuModelForm(request.POST)

    if form.is_valid():
        form.save()

        return redirect(urls.memory_reverse(request, 'rbac:menu_list'))

    return render(request, 'rbac/role_change.html', {'form': form})


def second_menu_edit(request, pk):
    '''
    编辑二级菜单
    :param request:
    :param pk:
    :return:
    '''
    permission_obj = models.Permission.objects.filter(pid=pk).first()

    if not permission_obj:
        return HttpResponse('菜单不存在!')

    if request.method == 'GET':
        form = menu.SecondMenuModelForm(instance=permission_obj)

        return render(request, 'rbac/role_change.html', {'form': form})

    form = menu.SecondMenuModelForm(instance=permission_obj, data=request.POST)

    if form.is_valid():
        form.save()

        return redirect(urls.memory_reverse(request, 'rbac:menu_list'))

    return render(request, 'rbac/role_change.html', {'form': form})


def second_menu_del(request, pk):
    '''
    删除二级菜单
    :param request:
    :param pk:
    :return:
    '''
    url = urls.memory_reverse(request, 'rbac:menu_list')
    if request.method == 'GET':
        return render(request, 'rbac/delete.html', {'cancel': url})

    models.Permission.objects.filter(pid=pk).delete()

    return redirect(url)


def permission_add(request, second_menu_id):
    '''
    增加权限
    :param request:
    :param second_menu_id:
    :return:
    '''

    if request.method == 'GET':
        form = menu.PermissionModelForm()

        return render(request, 'rbac/role_change.html', {'form': form})

    form = menu.PermissionModelForm(request.POST)

    if form.is_valid():
        second_menu_obj = models.Permission.objects.filter(pid=second_menu_id).first()

        if not second_menu_obj:
            return HttpResponse('二级菜单不存在!')

        form.instance.p_id = second_menu_obj  # 给新增权限绑定二级菜单
        form.save()

        return redirect(urls.memory_reverse(request, 'rbac:menu_list'))

    return render(request, 'rbac/role_change.html', {'form': form})


def permission_edit(request, pk):
    '''
    编辑权限
    :param request:
    :param pk:
    :return:
    '''
    permission_obj = models.Permission.objects.filter(pid=pk).first()

    if not permission_obj:
        return HttpResponse('菜单不存在!')

    if request.method == 'GET':
        form = menu.PermissionModelForm(instance=permission_obj)

        return render(request, 'rbac/role_change.html', {'form': form})

    form = menu.PermissionModelForm(instance=permission_obj, data=request.POST)

    if form.is_valid():
        form.save()

        return redirect(urls.memory_reverse(request, 'rbac:menu_list'))

    return render(request, 'rbac/role_change.html', {'form': form})


def permission_del(request, pk):
    '''
    删除权限
    :param request:
    :param pk:
    :return:
    '''
    url = urls.memory_reverse(request, 'rbac:menu_list')
    if request.method == 'GET':
        return render(request, 'rbac/delete.html', {'cancel': url})

    models.Permission.objects.filter(pid=pk).delete()

    return redirect(url)


def multi_permission(request):
    '''
    批量增改权限
    :param request: 
    :return: 
    '''

    post_type = request.GET.get('type')

    formset_add_class = formset_factory(menu.MultiAddPermissionsForm, extra=0)
    generate_formset = None

    # 批量新增权限
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
                models.Permission.objects.bulk_create(obj_list, batch_size=50) # batch_size=50设置一次批量增加条数
        else:
            generate_formset = formset

    # 批量更新权限
    update_formset_class = formset_factory(menu.MultiUpdatePermissionsForm, extra=0)
    update_formset = None
    if request.method == 'POST' and post_type == 'update':

        formset = update_formset_class(request.POST)
        
        if formset.is_valid():
            
            post_update_list = formset.cleaned_data
            for i in range(0, formset.total_form_count()):
                
                update_row = post_update_list[i]

                permission_id = update_row.pop('pid')
                try:
                    update_obj = models.Permission.objects.filter(pid=permission_id).first()
                    for k, v in update_row.items():
                        setattr(update_obj, k, v)
                        
                    update_obj.validate_unique()
                    update_obj.save()
                except Exception as e:
                    formset.errors[i].update(e)
                    update_formset = formset
        else:
            update_formset = formset

    # 自动发现项目中所有的url
    auto_get_all_url = routes.get_all_url_dict()
    router_name_set = set(auto_get_all_url.keys())

    # 获取数据库中所有的url
    permission_list = models.Permission.objects.all().values('pid', 'title', 'name', 'url', 'menu_id', 'p_id_id')
    permission_dict = OrderedDict()

    for row in permission_list:
        permission_dict[row['name']] = row

    permission_name_set = set(permission_dict.keys())

    for name, value in permission_dict.items():
        router_row_dict = auto_get_all_url.get(name)

        if not router_row_dict:
            continue

        if value['url'] != router_row_dict['url']:
            value['url'] = '路由和数据库不一致'

    # 获取待操作权限名称列表
    # 待添加权限
    if not generate_formset:
        generate_name_list = router_name_set - permission_name_set
        generate_formset = formset_add_class(
            initial=[row_dict for name, row_dict in auto_get_all_url.items() if name in generate_name_list])

    # 待删除权限
    delete_name_list = permission_name_set - router_name_set
    delete_row_list = [row_dict for name, row_dict in permission_dict.items() if name in delete_name_list]
   
    # 待更新权限
    if not update_formset:
        update_name_list = router_name_set & permission_name_set
        update_formset = update_formset_class(
            initial=[row_dict for name, row_dict in permission_dict.items() if name in update_name_list])

    return render(request, 'rbac/multi_permission.html', {
        'generate_formset': generate_formset, 
        'delete_row_list': delete_row_list,
        'update_formset': update_formset})


def multi_permission_del(request, pk):
    '''
    删除批量权限
    :param request: 
    :param pk: 
    :return: 
    '''

    url = urls.memory_reverse(request, 'rbac:multi_permission')
    if request.method == 'GET':
        return render(request, 'rbac/delete.html', {'cancel': url})

    models.Permission.objects.filter(pid=pk).delete()

    return redirect(url)


def distribute_permission(request):
    '''
    用户权限分配
    :param request: 
    :return: 
    '''
        
    # ######获取用户权限信息######
    role_id = request.GET.get('rid')
    user_id = request.GET.get('uid')
    role_obj = models.Role.objects.filter(rid=role_id).first()
    user_obj = models.UserInfo.objects.filter(id=user_id).first()
    if not user_obj:
        user_id = None
    if not role_obj:
        role_id = None

    # ###############处理用户提交过来的角色和权限修改信息##################

    if request.method == 'POST' and request.POST.get('type') == 'role':
        chang_role_list = request.POST.getlist('role')

        if not user_obj:
            return HttpResponse('请先选择用户，再分配角色!')
        user_obj.roles.set(chang_role_list)

    if request.method == 'POST' and request.POST.get('type') == 'permission':

        chang_permission_list = request.POST.getlist('permissions')

        if not role_obj:
            return HttpResponse('请先选择角色，再分配权限!')
        role_obj.permissions.set(chang_permission_list)

    # 如果选中了角色优先显示角色权限，没有选中角色显示用户权限

    if role_obj:
        user_permission = role_obj.permissions.all()
        user_permission_dict = {item.pid: None for item in user_permission}
    elif user_obj:
        user_permission = user_obj.roles.values('permissions').filter(permissions__pid__isnull=False).distinct()
        user_permission_dict = {item['permissions']: None for item in user_permission}
    else:

        user_permission_dict = {}

    # 获取当前用户拥有的角色
    if user_id:
        user_role = user_obj.roles.all()
    else:
        user_role = []
    user_role_dict = {item.rid: None for item in user_role}

    # #######获取所有的菜单和权限#############

    all_user_list = models.UserInfo.objects.all()
    all_role_list = models.Role.objects.all()

    # 所有的一级菜单
    all_menu_list = models.Menu.objects.all().values('mid', 'title')
    all_menu_dict = {}

    for item in all_menu_list:
        item['children'] = []
        all_menu_dict[item['mid']] = item

    # 所有的二级菜单
    all_second_menu_list = models.Permission.objects.filter(menu__isnull=False).values('pid', 'title', 'menu_id')
    all_second_menu_dict = {}
    for item in all_second_menu_list:

        item['children'] = []
        all_second_menu_dict[item['pid']] = item

        mid = item['menu_id']
        if mid in all_menu_dict:
            all_menu_dict[mid]['children'].append(item)

    # 所有的三级菜单
    all_permission_list = models.Permission.objects.filter(menu__isnull=True).values('pid', 'title', 'p_id_id')

    for row in all_permission_list:

        pid = row['p_id_id']
        if pid not in all_second_menu_dict:
            continue

        all_second_menu_dict[pid]['children'].append(row)

    return render(request, 'rbac/distribute_permission.html', {
        'user_list': all_user_list,
        'role_id': role_id,
        'role_list': all_role_list,
        'all_menu_list': all_menu_list,
        'user_id': user_id,
        'user_role_dict': user_role_dict,
        'user_permission_dict':  user_permission_dict,
    })



