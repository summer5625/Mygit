from django.shortcuts import render, HttpResponse
from django import forms
from django.forms import formset_factory

from app01 import models


class PerssionForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput())
    url = forms.CharField(widget=forms.TextInput())
    name = forms.CharField(widget=forms.TextInput())
    menu_id = forms.ChoiceField(
        choices=[(None, '-----')],  # 没有值时默认填充值
        widget=forms.Select(),
        required=False,  # 表明该字段是不是能为空值
    )

    p_id_id = forms.ChoiceField(
        choices=[(None, '-----')],
        widget=forms.Select(),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['menu_id'].choices += models.Menu.objects.values_list('mid', 'title')  # 将关联菜单表中的信息填充到下拉框
        self.fields['p_id_id'].choices += models.Permission.objects.filter(pid__isnull=True).exclude(
            menu__isnull=True).values_list('pid', 'title')


class UpdatePerssionForm(forms.Form):
    pid = forms.IntegerField(widget=forms.HiddenInput())
    title = forms.CharField(widget=forms.TextInput())
    url = forms.CharField(widget=forms.TextInput())
    name = forms.CharField(widget=forms.TextInput())
    menu_id = forms.ChoiceField(
        choices=[(None, '-----')],  # 没有值时默认填充值
        widget=forms.Select(),
        required=False,  # 表明该字段是不是能为空值
    )

    p_id_id = forms.ChoiceField(
        choices=[(None, '-----')],
        widget=forms.Select(),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['menu_id'].choices += models.Menu.objects.values_list('mid', 'title')  # 将关联菜单表中的信息填充到下拉框
        self.fields['p_id_id'].choices += models.Permission.objects.filter(pid__isnull=True).exclude(
            menu__isnull=True).values_list('pid', 'title')


def add(request):
    formset_class = formset_factory(PerssionForm, extra=2)  # 创建formset类,extra=2表示生成5个表单

    if request.method == 'GET':
        formset = formset_class()  # 实例化formset_class

        return render(request, 'add.html', {'formset': formset})

    formset = formset_class(data=request.POST)
    if formset.is_valid():

        flag = True
        post_row_list = formset.cleaned_data  # 检查formset中有没有错误信息，并获取用户提交的无异常信息

        for i in range(0, formset.total_form_count()):  # formset.total_form_count()获取用户提交信息的长度，即有几组有效信息
            row = post_row_list[i]  # 也可以写成formset.cleaned_data,这样写造成的问题是，当给提交异常数据绑定错误信息绑定错误信息后
            # 在对下体条信息进行检查时会将该异常的数据从cleaned_data中剔除，即每次只执行cleaned_data时都会检查是否有异常信息

            if not row:  # 检查用户是否输入了信息
                continue

            try:
                obj = models.Permission(**row)  # 将用户提交的信息保存到数据库
                obj.validate_unique()  # 检查数据库中唯一字段是否有重复，有重复抛出异常
                obj.save()

            except Exception as e:

                formset.errors[i].update(e)  # 将抛出的字段唯一异常更新到错误提示中
                flag = False

        if flag:
            return HttpResponse('提交成功!')

        else:
            return render(request, 'add.html', {'formset': formset})

    return render(request, 'add.html', {'formset': formset})


def edit(request):
    formset_class = formset_factory(UpdatePerssionForm, extra=0)  # 创建formset类,extra=0表示不添加空白行

    if request.method == 'GET':
        formset = formset_class(initial=models.Permission.objects.all().values('pid', 'title', 'name', 'url', 'menu_id',
                                                                               'p_id_id'))  # 实例化formset_class

        return render(request, 'edit.html', {'formset': formset})

    formset = formset_class(data=request.POST)
    if formset.is_valid():

        flag = True
        post_row_list = formset.cleaned_data  # 检查formset中有没有错误信息，并获取用户提交的无异常信息

        for i in range(0, formset.total_form_count()):  # formset.total_form_count()获取用户提交信息的长度，即有几组有效信息
            row = post_row_list[i]

            if not row:  # 检查用户是否输入了信息
                continue
            permission_id = row.pop('pid')
            try:
                permission_obj = models.Permission.objects.filter(pid=permission_id).first()

                for key, value in row.itema():  # 将修改后数据保存到数据库
                    setattr(permission_obj, key, value)

                permission_obj.validate_unique()  # 检查数据库中唯一字段是否有重复，有重复抛出异常
                permission_obj.save()

            except Exception as e:

                formset.errors[i].update(e)  # 将抛出的字段唯一异常更新到错误提示中
                flag = False

        if flag:
            return HttpResponse('提交成功!')

        else:
            return render(request, 'edit.html', {'formset': formset})

    return render(request, 'edit.html', {'formset': formset})
