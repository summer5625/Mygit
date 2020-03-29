# -*- coding: utf-8 -*-
# @Time    : 2020/1/30  19:21
# @Author  : XiaTian
# @File    : menu.py
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError
from django import forms
from ppp import models
from ppp.forms import base


icon_list = ['fa fa-address-book', 'fa fa-address-book-o', 'fa fa-address-card', 'fa fa-address-card-o', 'fa fa-adjust',
             'fa fa-american-sign-language-interpreting', 'fa fa-anchor', 'fa fa-archive', 'fa fa-area-chart',
             'fa fa-arrows', 'fa fa-arrows-h', 'fa fa-arrows-v', 'fa fa-asl-interpreting',
             'fa fa-assistive-listening-systems', 'fa fa-asterisk', 'fa fa-at', 'fa fa-audio-description',
             'fa fa-automobile', 'fa fa-balance-scale', 'fa fa-ban', 'fa fa-bank', 'fa fa-bar-chart',
             'fa fa-bar-chart-o', 'fa fa-barcode', 'fa fa-bars', 'fa fa-bath', 'fa fa-bathtub', 'fa fa-battery',
             'fa fa-battery-0', 'fa fa-battery-1']

c = []
for i in icon_list:
    d = i.split(' ')
    c.append((d[0], d[1]))
icons = []
for i in c:
    str = "<i class='%s %s' aira-hidden='true'></i>" % (i[0], i[1])
    icons.append([i[1], mark_safe(str)])


# 一级菜单
class MenuModelForm(forms.ModelForm):
    
    class Meta:
        
        model = models.Menu
        fields = ['title', 'icon']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'icon': forms.RadioSelect(choices=icons)
        }

        error_messages = {
            'icon': {'required': '请选择图标'}
        }


# 二级菜单
class SecondMenu(base.BootStrapModelForm):
    
    class Meta:
        model = models.Permission
        exclude = ['p_id']
        
    def clean_url(self):
        url = self.cleaned_data.get('url')
        url_obj = models.Permission.objects.filter(url=url)
        if url_obj:
            raise ValidationError('url已存在')
        
        return url
    

# 权限菜单
class PermissionModel(base.BootStrapModelForm):

    class Meta:
        model = models.Permission
        fields = ['title', 'url', 'name']


# 批量操作权限
class MultiAddPermission(forms.Form):
    
    title = forms.CharField(widget=forms.TextInput())
    url = forms.CharField(widget=forms.TextInput())
    name = forms.CharField(widget=forms.TextInput())
    menu_id = forms.ChoiceField(choices=[(None, '-----')], widget=forms.Select(), required=False)
    p_id_id = forms.ChoiceField(choices=[(None, '-----')], widget=forms.Select(), required=False)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['menu_id'].choices += models.Menu.objects.values_list('id', 'title')
        self.fields['p_id_id'].choices += models.Permission.objects.filter(id__isnull=False).exclude(
            menu__isnull=True).values_list('id', 'title')


# 批量更新权限
class MultiUpdatePermission(forms.Form):
    
    id = forms.IntegerField(widget=forms.HiddenInput())
    title = forms.CharField(widget=forms.TextInput())
    url = forms.CharField(widget=forms.TextInput())
    name = forms.CharField(widget=forms.TextInput())
    menu_id = forms.ChoiceField(choices=[(None, '----')], widget=forms.Select(), required=False)
    p_id_id = forms.ChoiceField(choices=[(None, '----')], widget=forms.Select(), required=False)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['menu_id'].choices += models.Menu.objects.values_list('id', 'title')
        self.fields['p_id_id'].choices += models.Permission.objects.filter(id__isnull=False).exclude(
            menu__isnull=True).values_list('id', 'title')




















