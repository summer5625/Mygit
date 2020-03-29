# -*- coding: utf-8 -*-
# @Time    : 2020/2/7  16:31
# @Author  : XiaTian
# @File    : handle_table.py
from types import FunctionType
import functools
from django.urls import path, re_path, reverse
from django.shortcuts import HttpResponse, render, redirect
from django.utils.safestring import mark_safe
from django.http import QueryDict
from django import forms
from django.db.models import Q, ForeignKey, ManyToManyField
from skk.utils.pagination import Pagination


class StarkModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(StarkModelForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


def get_choice_text(title, field):
    
    def inner(self, obj=None, is_header=None):
        if is_header:
            return title
        method = 'get_%s_display' % field
        return getattr(obj, method)()

    return inner


class SearchGroupRow(object):

    def __init__(self, queryset_or_tuple, option, title, query_dict):

        self.queryset_or_tuple = queryset_or_tuple
        self.option = option
        self.title = title
        self.query_dict = query_dict

    def __iter__(self):

        yield '<div class="whole">'
        yield self.title + ':'
        yield '</div>'

        yield '<div class="others">'
        total_query_dict = self.query_dict.copy()
        total_query_dict._mutable = True
        origin_value_list = self.query_dict.getlist(self.option.field)
        if not origin_value_list:
            yield "<a href='?%s' class='active'>全部</a>" % total_query_dict.urlencode()
        else:
            total_query_dict.pop(self.option.field)
            yield "<a href='?%s'>全部</a>" % total_query_dict.urlencode()

        for item in self.queryset_or_tuple:
            text = self.option.get_text(item)
            value = str(self.option.get_value(item))

            query_dict = self.query_dict.copy()
            query_dict._mutable = True

            if not self.option.is_multi:
                query_dict[self.option.field] = value

                if value in origin_value_list:
                    query_dict.pop(self.option.field)
                    yield "<a href='?%s' class='active'>%s</a>" % (query_dict.urlencode(), text)
                else:
                    yield "<a href='?%s'>%s</a>" % (query_dict.urlencode(), text)
            else:
                multi_value_list = query_dict.getlist(self.option.field)
                if value in multi_value_list:
                    multi_value_list.remove(value)
                    query_dict.setlist(self.option.field, multi_value_list)

                    yield "<a href='?%s' class='active'>%s</a>" % (query_dict.urlencode(), text)
                else:
                    multi_value_list.append(value)
                    query_dict.setlist(self.option.field, multi_value_list)
                    
                    yield "<a href='?%s'>%s</a>" % (query_dict.urlencode(), text)
                    
        yield '</div>'


class SearchOption:

    def __init__(self, field, db_condition=None, text_func=None, value_func=None, is_multi=False):

        self.field = field

        if not db_condition:
            db_condition = {}
        self.db_condition = db_condition
        self.text_func = text_func
        self.is_choices = False
        self.value_func = value_func
        self.is_multi = is_multi

    def get_db_condition(self, request, *args, **kwargs):

        return self.db_condition

    def get_queryset_or_tuple(self, model_class, request, *args, **kwargs):

        filed_obj = model_class._meta.get_field(self.field)
        title = filed_obj.verbose_name
        if isinstance(filed_obj, ForeignKey) or isinstance(filed_obj, ManyToManyField):
            db_condition = self.get_db_condition(request, *args, **kwargs)
            return SearchGroupRow(filed_obj.related_model.objects.filter(**db_condition), self, title, request.GET)
        else:
            self.is_choices = True
            return SearchGroupRow(filed_obj.choices, self, title, request.GET)

    def get_text(self, field_obj):

        if self.text_func:
            return self.text_func(field_obj)
        if self.is_choices:
            return field_obj[1]
        else:
            return str(field_obj)

    def get_value(self, field_obj):

        if self.value_func:
            return self.value_func(field_obj)
        if self.is_choices:
            return field_obj[0]
        else:
            return field_obj.pk


class Handler(object):
    list_display = []
    per_page_count = 10
    has_add_btn = None
    order_list = None
    model_form_class = None
    search_list = []
    action_list = []
    search_group = []

    def __init__(self, stark_site, model_class, prev):

        self.stark_site = stark_site
        self.model_class = model_class
        self.prev = prev
        self.request = None

    def get_list_display(self):

        value = []
        value.extend(self.list_display)
        return value

    def display_checkbox(self, obj=None, is_header=None):

        if is_header:
            return '选择'

        return mark_safe("<input type='checkbox' name='pk' value='%s'>" % obj.pk)

    def display_edit(self, obj=None, is_header=None):

        if is_header:
            return '编辑'
        return mark_safe("<a href='%s'>编辑</a>" % self.reverse_edit_url(pk=obj.pk))

    def display_del(self, obj=None, is_header=None):

        if is_header:
            return '删除'
        return mark_safe("<a href='%s'>删除</a>" % self.reverse_del_url(pk=obj.pk))

    def get_model_form_class(self):

        if self.model_form_class:
            return self.model_form_class

        class DynamicModelForm(StarkModelForm):
            class Meta:
                model = self.model_class
                fields = '__all__'

        return DynamicModelForm

    def save(self, form, is_update=False):
        form.save()

    def get_add_btn(self):

        if self.has_add_btn:
            return '<a class="btn btn-primary" href="%s">添加</a>' % self.reverse_add_url()
        return None

    def get_action_list(self):

        return self.action_list

    def get_order_list(self):

        return self.order_list or ['-id', ]

    def get_search_group_list(self):

        return self.search_group

    def get_search_group_condition(self, request):

        condition = {}
        for option in self.get_search_group_list():

            if option.is_multi:
                values_list = request.GET.getlist(option.field)

                if not values_list:
                    continue
                condition['%s__in' % option.field] = values_list
            else:
                value = request.GET.get(option.field)
                if not value:
                    continue
                condition[option.field] = value

        return condition

    def reverse_list_url(self):

        name = '%s:%s' % (self.stark_site.namespace, self.get_list_url_name)
        base_url = reverse(name)
        param = self.request.GET.get('_filter')
        if not param:
            list_url = base_url
        else:
            list_url = '%s?%s' % (base_url, param)

        return list_url

    def reverse_add_url(self):

        name = '%s:%s' % (self.stark_site.namespace, self.get_add_url_name)
        base_url = reverse(name)

        if not self.request.GET:
            add_url = base_url
        else:
            param = self.request.GET.urlencode()
            new_query_dict = QueryDict(mutable=True)
            new_query_dict['_filter'] = param
            add_url = '%s?%s' % (base_url, new_query_dict.urlencode())

        return add_url

    def reverse_edit_url(self, *args, **kwargs):

        name = '%s:%s' % (self.stark_site.namespace, self.get_edit_url_name)
        base_url = reverse(name, args=args, kwargs=kwargs)

        if not self.request.GET:
            edit_url = base_url
        else:
            param = self.request.GET.urlencode()
            new_query_dict = QueryDict(mutable=True)
            new_query_dict['_filter'] = param
            edit_url = '%s?%s' % (base_url, new_query_dict.urlencode())

        return edit_url

    def reverse_del_url(self, *args, **kwargs):

        name = '%s:%s' % (self.stark_site.namespace, self.get_del_url_name)
        base_url = reverse(name, args=args, kwargs=kwargs)

        if not self.request.GET:
            del_url = base_url
        else:
            param = self.request.GET.urlencode()
            new_query_dict = QueryDict(mutable=True)
            new_query_dict['_filter'] = param
            del_url = '%s?%s' % (base_url, new_query_dict.urlencode())

        return del_url

    def multi_delete(self, request, *args, **kwargs):

        pk_list = request.POST.getlist('pk')
        self.model_class.objects.filter(id__in=pk_list).delete()

    multi_delete.text = '批量删除'

    def list_view(self, request, *args, **kwargs):

        # 批量处理
        action_list = self.get_action_list()
        action_dict = {func.__name__: func.text for func in action_list}
        print(action_dict)
        if request.method == 'POST':
            action_func_name = request.POST.get('action')
            if action_func_name and action_func_name in action_dict:
                action_response = getattr(self, action_func_name)(request, *args, **kwargs)
                if action_response:
                    return action_response

        # 模糊查询
        search_list = self.search_list
        search_value = request.GET.get('q', '')

        conn = Q()
        conn.connector = 'OR'
        for item in search_list:
            conn.children.append((item, search_value))

        # 排序
        order_list = self.get_order_list()
        search_group_condition = self.get_search_group_condition(request)
        queryset = self.model_class.objects.filter(conn).filter(**search_group_condition).order_by(*order_list)

        # 处理分页
        all_count = queryset.count()
        query_params = request.GET.copy()
        query_params._mutable = True

        pager = Pagination(
            current_page=request.GET.get('page'),
            all_count=all_count,
            base_url=request.path_info,
            query_params=query_params,
            per_page=self.per_page_count
        )
        data_list = queryset[pager.start:pager.end]

        # 处理表头
        header_list = []
        list_display = self.get_list_display()

        if list_display:
            for key in list_display:
                if isinstance(key, FunctionType):
                    verbose_name = key(self, obj=None, is_header=True)
                else:
                    verbose_name = self.model_class._meta.get_field(key).verbose_name
                header_list.append(verbose_name)
        else:
            header_list.append(self.model_class._meta.model_name)

        # 获取表格内容
        body_list = []
        for row in data_list:
            temp_list = []
            if list_display:
                for key in list_display:
                    if isinstance(key, FunctionType):
                        temp_list.append(key(self, row, is_header=False))
                    else:
                        temp_list.append(getattr(row, key))
            else:
                temp_list.append(row)
            body_list.append(temp_list)

        # 组合搜索
        search_group = self.get_search_group_list()
        search_group_list = []
        for option_obj in search_group:
            row = option_obj.get_queryset_or_tuple(self.model_class, request, *args, **kwargs)
            search_group_list.append(row)

        return render(request, 'stark/list.html', {
            'data_list': data_list,
            'header_list': header_list,
            'body_list': body_list,
            'pager': pager,
            'add_btn': self.get_add_btn(),
            'search_value': search_value,
            'search_list': search_list,
            'action_dict': action_dict,
            'search_group_list': search_group_list
        })

    def add_view(self, request, *args, **kwargs):

        model_form_class = self.get_model_form_class()
        if request.method == 'GET':
            form = model_form_class()
            return render(request, 'stark/change.html', {'form': form})

        form = model_form_class(data=request.POST)
        if form.is_valid():
            self.save(form, is_update=False)

            return redirect(self.reverse_list_url())
        return render(request, 'stark/change.html', {'form': form})

    def edit_view(self, request, pk, *args, **kwargs):

        obj = self.model_class.objects.filter(pk=pk).first()
        if not obj:
            return HttpResponse('请选择要修改的信息!')
        model_from_class = self.get_model_form_class()
        if request.method == 'GET':
            form = model_from_class(instance=obj)
            return render(request, 'stark/change.html', {'form': form})
        form = model_from_class(data=request.POST, instance=obj)
        if form.is_valid():
            self.save(form, is_update=False)
            return redirect(self.reverse_list_url())
        return render(request, 'stark/change.html', {'form': form})

    def del_view(self, request, pk, *args, **kwargs):

        if request.method == 'GET':
            return render(request, 'stark/delete.html', {'cancel': self.reverse_list_url()})

        self.model_class.objects.filter(pk=pk).delete()

        return redirect(self.reverse_list_url())

    def wrapper(self, func):

        @functools.wraps(func)
        def inner(request, *args, **kwargs):
            self.request = request

            return func(request, *args, **kwargs)

        return inner

    def extra_urls(self):

        return []

    def get_url_name(self, param):

        app_label, model_name = self.model_class._meta.app_label, self.model_class._meta.model_name

        if self.prev:
            return '%s_%s_%s_%s' % (app_label, model_name, self.prev, param)
        return '%s_%s_%s' % (app_label, model_name, param)

    @property
    def get_list_url_name(self):
        return self.get_url_name('list')

    @property
    def get_add_url_name(self):
        return self.get_url_name('add')

    @property
    def get_edit_url_name(self):
        return self.get_url_name('edit')

    @property
    def get_del_url_name(self):
        return self.get_url_name('del')

    def get_urls(self):

        patterns = [
            path('list/', self.wrapper(self.list_view), name=self.get_list_url_name),
            path('add/', self.wrapper(self.add_view), name=self.get_add_url_name),
            re_path(r'^edit/(?P<pk>\d+)/$', self.wrapper(self.edit_view), name=self.get_edit_url_name),
            re_path(r'^del/(?P<pk>\d+)/$', self.wrapper(self.del_view), name=self.get_del_url_name)
        ]

        patterns.extend(self.extra_urls())

        return patterns


class StarkSite(object):

    def __init__(self):
        self._registry = []
        self.app_name = 'skk'
        self.namespace = 'skk'

    def register(self, model_class, handler_class=None, prev=None):

        if not handler_class:
            handler_class = Handler

        self._registry.append({
            'model_class': model_class,
            'handler_class': handler_class(self, model_class, prev),
            'prev': prev
        })

    def get_url(self):

        patterns = []

        for item in self._registry:

            model_class = item['model_class']
            handler = item['handler_class']
            prev = item['prev']
            app_label = model_class._meta.app_label
            model_name = model_class._meta.model_name

            if prev:
                patterns.append(path('%s/%s/%s/' % (app_label, model_name, prev), (handler.get_urls(), None, None)))
            else:
                patterns.append(path('%s/%s/' % (app_label, model_name), (handler.get_urls(), None, None)))

        return patterns

    @property
    def urls(self):
        return self.get_url(), self.app_name, self.namespace


site = StarkSite()
