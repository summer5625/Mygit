# -*- coding: utf-8 -*-
# @Time    : 2019/11/3  20:56
# @Author  : XiaTian
# @File    : handle_table.py
from types import FunctionType  # 检测是不是一个函数
import functools

from django.urls import path, re_path, reverse
from django.shortcuts import HttpResponse, render, redirect
from django.utils.safestring import mark_safe
from django.http import QueryDict
from django import forms
from django.db.models import Q, ForeignKey, ManyToManyField

from stark.utils.pagination import Pagination


class StarkModelForm(forms.ModelForm):
    '''
    表单的基类
    '''

    def __init__(self, *args, **kwargs):
        super(StarkModelForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


def get_choice_text(title, field):
    '''
    对于Stark组件中定义列时，choice如果想要显示中文信息，调用此方法即可。
    :param title:希望页面显示的表头
    :param field:字段名称
    :return:
    '''

    def inner(self, obj=None, is_header=None, *args, **kwargs):
        if is_header:
            return title

        method = 'get_%s_display' % field

        return getattr(obj, method)()

    return inner


def get_datetime_text(title, field, time_format='%Y-%m-%d'):
    '''
    格式化日期
    :param title:
    :param field:
    :return:
    '''

    def inner(self, obj=None, is_header=None, *args, **kwargs):
        if is_header:
            return title
        datetime_value = getattr(obj, field)

        return datetime_value.strftime(time_format)

    return inner


def get_m2m_text(title, field):
    '''
    获取数据库中m2m的文本信息
    :param title:
    :param field:
    :return:
    '''

    def inner(self, obj=None, is_header=None, *args, **kwargs):
        if is_header:
            return title

        queryset = getattr(obj, field).all()
        text_list = [str(row) for row in queryset]
        return ','.join(text_list)

    return inner


# 生成筛选的按钮
class SearchGroupRow(object):

    def __init__(self, queryset_or_tuple, option, title, query_dict):
        '''

        :param queryset_or_tuple: 传递的字段对象
        :param option: 筛选的配置对象
        :param title: 字段在数据库中的标题verbose_name
        '''
        self.queryset_or_tuple = queryset_or_tuple
        self.option = option
        self.title = title
        self.query_dict = query_dict

    def __iter__(self):
        '''
        生成用户筛选按钮上显示的文字
        :return:
        '''

        yield '<div class="whole">'
        yield self.title + ':'
        yield '</div>'

        yield '<div class="others">'
        total_query_dict = self.query_dict.copy()
        total_query_dict._mutable = True
        origin_value_list = self.query_dict.getlist(self.option.field)  # 选中的筛选按钮
        if not origin_value_list:  # 用户没有选择时默认选择了全部
            yield "<a href='?%s' class='active'>全部</a>" % total_query_dict.urlencode()
        else:
            total_query_dict.pop(self.option.field)
            yield "<a href='?%s'>全部</a>" % total_query_dict.urlencode()

        for item in self.queryset_or_tuple:
            text = self.option.get_text(item)
            value = str(self.option.get_value(item))

            # 将request中的值深拷贝一份，然后在对request值进行修改，并且不会影响其他函数里面的request
            query_dict = self.query_dict.copy()  # 用户选中的值
            query_dict._mutable = True  # 将其设置为可以修改，query_dict值默认是不可以修改的

            if not self.option.is_multi:  # 不支持多选
                query_dict[self.option.field] = value  # 构造按钮的url

                if value in origin_value_list:
                    query_dict.pop(self.option.field)  # 用户再次点击相同按钮就删除选中按钮对应的请求
                    yield "<a href='?%s' class='active'>%s</a>" % (query_dict.urlencode(), text)
                else:
                    yield "<a href='?%s'>%s</a>" % (query_dict.urlencode(), text)
            else:  # 支持多选
                multi_value_list = query_dict.getlist(self.option.field)

                if value in multi_value_list:
                    multi_value_list.remove(value)  # 选中后，再次点击就取消选中
                    query_dict.setlist(self.option.field, multi_value_list)

                    yield "<a href='?%s' class='active'>%s</a>" % (query_dict.urlencode(), text)

                else:
                    multi_value_list.append(value)  # 没有选中，点击后就添加进来
                    query_dict.setlist(self.option.field, multi_value_list)

                    yield "<a href='?%s'>%s</a>" % (query_dict.urlencode(), text)

        yield '</div>'


# 获取组合搜索条件
class SearchOption:

    def __init__(self, field, db_condition=None, text_func=None, value_func=None, is_multi=False):
        '''

        :param field: 数据库中关联字段的对象
        :param db_condition: 关联字段筛选的限制条件
        :param text_func: 用户自定义筛选按钮应该显示的文字
        '''

        self.field = field

        if not db_condition:
            db_condition = {}

        self.db_condition = db_condition

        self.text_func = text_func

        self.is_choice = False  # 判断数据库中的字段是不是choice类型

        self.value_func = value_func  # 用户定义的按钮的默认值

        self.is_multi = is_multi  # 是否支持组合搜索多选

    def get_db_condition(self, request, *args, **kwargs):
        '''
        获取用户自定义的搜索条件
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        return self.db_condition

    def get_queryset_or_tuple(self, model_class, request, *args, **kwargs):
        '''
        根据用户定义的搜索条件获取符合条件的值
        :param model_class:数据库中的表对象
        :param request:用户请求
        :param args:
        :param kwargs:
        :return:
        '''

        field_obj = model_class._meta.get_field(self.field)  # 字段对象
        title = field_obj.verbose_name
        # 判断获取的字段对象是一对多还是多对多的字段
        if isinstance(field_obj, ForeignKey) or isinstance(field_obj, ManyToManyField):
            # 获取关联表中的数据
            db_condition = self.get_db_condition(request, *args, **kwargs)
            return SearchGroupRow(field_obj.related_model.objects.filter(**db_condition), self, title, request.GET)
        else:
            # 获取选choice中的数据
            self.is_choice = True
            return SearchGroupRow(field_obj.choices, self, title, request.GET)

    def get_text(self, field_obj):
        '''
        获取用户自定义页面筛选按钮的显示文字
        :param field_obj:按钮字段对象
        :return:
        '''

        if self.text_func:  # 用户自定义了按钮的显示文字
            return self.text_func(field_obj)

        if self.is_choice:
            return field_obj[1]
        else:
            return str(field_obj)

    def get_value(self, field_obj):
        '''
        获取筛选按钮的对应的id
        :param field_obj: 按钮字段对象
        :return:
        '''

        if self.value_func:
            return self.value_func(field_obj)

        if self.is_choice:
            return field_obj[0]  # 返回按钮在数据库对应的id

        else:
            return field_obj.pk


class Handler(object):
    list_display = []

    per_page_count = 10

    has_add_btn = None

    order_list = None  # 排序规则

    model_form_class = None  # 给用户自定义form组件提供钩子

    search_list = []  # 模糊查询的条件

    action_list = []  # 批量操作功能列表

    search_group = []  # 组合搜索的条件列表

    list_template = None  # 列表页面模板

    change_template = None  # 添加编辑页面模板

    del_template = None  # 删除页面模板

    def __init__(self, stark_site, model_class, prev):
        '''

        :param model_class:表格的类名
        :param prev: 用户设置的前缀
        '''
        self.stark_site = stark_site
        self.model_class = model_class
        self.prev = prev
        self.request = None

    def get_list_display(self, request, *args, **kwargs):
        '''
        获取页面上应该显示的列，预留自定义扩展
        :return:
        '''

        value = []
        if self.list_display:
            value.extend(self.list_display)

        return value

    def display_checkbox(self, obj=None, is_header=None, *args, **kwargs):
        '''
        自定义批量选择按钮
        :param obj:
        :param is_header:
        :return:
        '''

        if is_header:
            return '选择'

        return mark_safe("<input type='checkbox' name='pk' value='%s'>" % obj.pk)

    def display_edit(self, obj=None, is_header=None, *args, **kwargs):
        '''
        自定义编辑按钮
        :param obj:
        :param is_header:
        :return:
        '''

        if is_header:
            return '编辑'

        return mark_safe("<a href='%s'>编辑</a>" % self.reverse_edit_url(pk=obj.pk, *args, **kwargs))

    def display_del(self, obj=None, is_header=None, *args, **kwargs):
        '''自定义删除按钮'''

        if is_header:
            return '删除'
        return mark_safe("<a href='%s'>删除</a>" % self.reverse_del_url(pk=obj.pk, *args, **kwargs))

    def display_edit_del(self, obj=None, is_header=None, *args, **kwargs):
        if is_header:
            return '操作'

        tpl = '<a href="%s">编辑</a> <a href="%s">删除</a>' % (
            self.reverse_edit_url(pk=obj.pk, *args, **kwargs), self.reverse_del_url(pk=obj.pk, *args, **kwargs))
        return mark_safe(tpl)

    def get_add_btn(self, request, *args, **kwargs):
        '''
        获取添加按钮
        :return: 
        '''

        if self.has_add_btn:
            return "<a class='btn btn-primary' href='%s'>添加</a>" % self.reverse_add_url(*args, **kwargs)

        return None

    def wrapper(self, func):
        '''
        装饰器 ，给需要得到request对象的函数
        :param func:
        :return:
        '''

        @functools.wraps(func)  # 保留原函数的原信息
        def inner(request, *args, **kwargs):
            self.request = request

            return func(request, *args, **kwargs)

        return inner

    def get_action_list(self):
        '''
        获取批量操作功能列表
        :return:
        '''
        return self.action_list

    def get_order_list(self):
        '''
        获取排序规则
        :return:
        '''
        return self.order_list or ['-id', ]

    def get_search_group_list(self):
        '''
        获取组合搜索的搜索条件
        :return:
        '''
        return self.search_group

    def get_search_group_condition(self, request):

        condition = {}
        for option in self.get_search_group_list():

            if option.is_multi:  # 支持多选
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

    def get_model_form_class(self, is_add, request, pk, *args, **kwargs):
        '''
        获取表单内容
        :return:
        '''
        if self.model_form_class:  # 用户自己定义了form组件就用用户的组件
            return self.model_form_class

        class DynamicModelForm(StarkModelForm):
            class Meta:
                model = self.model_class
                fields = '__all__'

        return DynamicModelForm

    def save(self, request, form, is_update, *args, **kwargs):
        '''
        将修改的信息保存到数据库，用户可以根据自己需要改写save方法
        :param form:表单
        :param is_update:是否要保存数据
        :return:
        '''

        form.save()

    def reverse_common_url(self, name, *args, **kwargs):
        '''
        生成url
        :param name: 要生成url的函数名称
        :param args:
        :param kwargs:
        :return:
        '''
        url_name = '%s:%s' % (self.stark_site.namespace, name)
        base_url = reverse(url_name, args=args, kwargs=kwargs)
        if not self.request.GET:  # 原来没有搜索条件，直接返回列表页面
            url = base_url
        else:
            param = self.request.GET.urlencode()
            new_query_dict = QueryDict(mutable=True)
            new_query_dict['_filter'] = param

            url = '%s?%s' % (base_url, new_query_dict.urlencode())

        return url

    def reverse_add_url(self, *args, **kwargs):
        '''
        生成带原搜索条件的添加的url
        :return:
        '''

        return self.reverse_common_url(self.get_add_url_name, *args, **kwargs)

    def reverse_list_url(self, *args, **kwargs):
        '''
        获取列表展示页面的url
        :return:
        '''

        return self.reverse_common_url(self.get_list_url_name, *args, **kwargs)

    def reverse_edit_url(self, *args, **kwargs):
        '''
        生成修改的url
        :param args:
        :param kwargs:
        :return:
        '''

        return self.reverse_common_url(self.get_edit_url_name, *args, **kwargs)

    def reverse_del_url(self, *args, **kwargs):
        '''
        生成删除的url
        :param args:
        :param kwargs:
        :return:
        '''

        return self.reverse_common_url(self.get_del_url_name, *args, **kwargs)

    def multi_delete(self, request, *args, **kwargs):
        pk_list = request.POST.getlist('pk')
        self.model_class.objects.filter(id__in=pk_list).delete()

    multi_delete.text = '批量删除'

    def get_queryset(self, request, *args, **kwargs):
        '''
        获取数据库中的数据，用户可以自定义筛选条件
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        return self.model_class.objects

    def list_view(self, request, *args, **kwargs):
        '''
        列表界面
        :param request:
        :return:
        '''

        # 处理批量操作功能
        action_list = self.get_action_list()
        action_dict = {func.__name__: func.text for func in action_list}  # 生成批量操作字典，方便前端调用

        if request.method == 'POST':
            action_func_name = request.POST.get('action')
            if action_func_name and action_func_name in action_dict:
                action_response = getattr(self, action_func_name)(request, *args, **kwargs)
                if action_response:  # 后续用户批量操作完后可以定义要跳转的地址
                    return action_response

        # 构造模糊查询的条件
        search_list = self.search_list

        search_value = request.GET.get('q', '')  # 如果用户提交了搜索信息就有，没有提交搜索信息，搜索信息就为空

        conn = Q()
        conn.connector = 'OR'  # 规定查询的条件，多个条件是或的关系
        for item in search_list:
            conn.children.append((item, search_value))  # 查询条件要是元组

        # 排序规则
        order_list = self.get_order_list()
        search_group_condition = self.get_search_group_condition(request)
        prev_queryset = self.get_queryset(request, *args, **kwargs)
        queryset = prev_queryset.filter(conn).filter(**search_group_condition).order_by(*order_list)

        # 处理分页
        all_count = queryset.count()
        query_params = request.GET.copy()
        query_params._mutable = True

        pager = Pagination(
            current_page=request.GET.get('page'),
            all_count=all_count,
            base_url=request.path_info,
            query_params=query_params,
            per_page=self.per_page_count,
        )

        data_list = queryset[pager.start:pager.end]

        # 处理表头
        header_list = []
        list_display = self.get_list_display(request, *args, **kwargs)

        if list_display:  # 如果定义了list_display表头就显示list_display里面定义的值对应的名称
            for key in list_display:

                if isinstance(key, FunctionType):
                    verbose_name = key(self, obj=None, is_header=True, *args, **kwargs)
                else:
                    verbose_name = self.model_class._meta.get_field(key).verbose_name
                header_list.append(verbose_name)

        else:  # 如果没定义list_display表头就显示表名称
            header_list.append(self.model_class._meta.model_name)

        # 获取表格内容
        # data_list = self.model_class.objects.all()
        body_list = []
        for row in data_list:

            temp_list = []
            if list_display:  # 如果定义了list_display表格内容就显示定义的内容

                for key in list_display:

                    if isinstance(key, FunctionType):

                        temp_list.append(key(self, row, is_header=False, *args, **kwargs))
                    else:
                        temp_list.append(getattr(row, key))

            else:  # 如果没定义list_display表格内容就显示对象名称
                temp_list.append(row)

            body_list.append(temp_list)

        # 组合搜索
        search_group = self.get_search_group_list()  # 实例化的SearchOption类的对象
        search_group_list = []
        for option_obj in search_group:
            # 根据用户配置的筛选条件到数据库中获取对应条件的关联的字段对象
            row = option_obj.get_queryset_or_tuple(self.model_class, request, *args, **kwargs)
            search_group_list.append(row)

        return render(request, self.list_template or 'stark/list.html',
                      {'data_list': data_list,
                       'header_list': header_list,
                       'body_list': body_list,
                       'pager': pager,
                       'add_btn': self.get_add_btn(request, *args, **kwargs),
                       'search_value': search_value,
                       'search_list': search_list,
                       'action_dict': action_dict,
                       'search_group_list': search_group_list,
                       })

    def add_view(self, request, *args, **kwargs):
        '''
        添加页面
        :param request:
        :return:
        '''
        model_form_class = self.get_model_form_class(True, request, None, *args, **kwargs)
        if request.method == 'GET':
            form = model_form_class()

            return render(request, self.change_template or 'stark/change.html', {'form': form})

        form = model_form_class(data=request.POST)

        if form.is_valid():
            response = self.save(request, form, is_update=False, *args, **kwargs)

            return response or redirect(self.reverse_list_url(*args, **kwargs))

        return render(request, self.change_template or 'stark/change.html', {'form': form})
    
    def change_object(self, request, pk, *args, **kwargs):
        '''
        定制筛选条件，防止非法入侵
        :param request: 
        :param pk: 
        :param args: 
        :param kwargs: 
        :return: 
        '''
        
        obj= self.model_class.objects.filter(pk=pk).first()
        return obj

    def edit_view(self, request, pk, *args, **kwargs):
        '''
        编辑页面
        :param request:
        :return:
        '''

        obj = self.change_object(request, pk, *args, **kwargs)
        if not obj:
            return HttpResponse('请选择要修改的信息!')

        model_form_class = self.get_model_form_class(False, request, pk, *args, **kwargs)
        if request.method == 'GET':
            form = model_form_class(instance=obj)
            return render(request, self.change_template or 'stark/change.html', {'form': form})

        form = model_form_class(data=request.POST, instance=obj)
        if form.is_valid():
            self.save(request, form, is_update=False, *args, **kwargs)

            return redirect(self.reverse_list_url(*args, **kwargs))
        return render(request, self.change_template or 'stark/change.html', {'form': form})
    
    def del_object(self, request, pk, *args, **kwargs):
        '''
        定制删除是的筛选条件
        :param request: 
        :param pk: 
        :param args: 
        :param kwargs: 
        :return: 
        '''

        self.model_class.objects.filter(pk=pk).delete()
        
    def del_view(self, request, pk, *args, **kwargs):
        '''
        删除页面
        :param request:
        :param pk:
        :return:
        '''

        if request.method == 'GET':
            return render(request, self.del_template or 'stark/delete.html',
                          {'cancel': self.reverse_list_url(*args, **kwargs)})

        response = self.del_object(request, pk, *args, **kwargs)

        return response or redirect(self.reverse_list_url(*args, **kwargs))

    def extra_urls(self):
        '''
        用户自定义的url
        :return:
        '''

        return []

    def get_url_name(self, param):
        '''
        获取url的别名
        :param param:
        :return:
        '''

        app_label, model_name = self.model_class._meta.app_label, self.model_class._meta.model_name

        if self.prev:
            return '%s_%s_%s_%s' % (app_label, model_name, self.prev, param)

        return '%s_%s_%s' % (app_label, model_name, param)

    @property
    def get_list_url_name(self):
        '''
        获取列表的url别名
        :return:
        '''
        return self.get_url_name('list')

    @property
    def get_add_url_name(self):
        '''
        获取添加的url别名
        :return:
        '''

        return self.get_url_name('add')

    @property
    def get_edit_url_name(self):
        '''
        获取编辑的url别名
        :return:
        '''

        return self.get_url_name('edit')

    @property
    def get_del_url_name(self):
        '''
        获取删除的url别名
        :return:
        '''

        return self.get_url_name('del')

    def get_urls(self):
        '''
        生成url
        :return:
        '''

        # url别名设置

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
        self.app_name = 'stark'
        self.namespace = 'stark'

    def register(self, model_class, handler_class=None, prev=None):
        '''

        :param model_class: 数据库中表名的类
        :param handler_class: 处理请求的视图函数
        :return:
        '''
        if not handler_class:
            handler_class = Handler

        self._registry.append({
            'model_class': model_class,
            'handler_class': handler_class(self, model_class, prev),
            'prev': prev})

    def get_url(self):
        '''
        生成url列表，需要拿到表名和app名称
        :return:
        '''
        patterns = []
        for item in self._registry:
            model_class = item['model_class']
            handler = item['handler_class']
            prev = item['prev']
            app_label = model_class._meta.app_label  # 获取app的名字
            model_name = model_class._meta.model_name  # 获取表名

            if prev:

                patterns.append(path('%s/%s/%s/' % (app_label, model_name, prev), (handler.get_urls(), None, None)))

            else:

                patterns.append(path('%s/%s/' % (app_label, model_name), (handler.get_urls(), None, None)))

        return patterns

    @property
    def urls(self):

        return self.get_url(), self.app_name, self.namespace


site = StarkSite()
