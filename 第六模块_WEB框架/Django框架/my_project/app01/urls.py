# -*- coding: utf-8 -*-
# @Time    : 2019/9/26  17:08
# @Author  : XiaTian
# @File    : urls.py

"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, register_converter #先引入re_path，相当用正则法则去匹配路径


from app01 import views
from app01 import ulconvert

#注册自定义转换器
register_converter(ulconvert.MonthConvert, 'mm') #第二个参数是给转换器名的名字


#路由配置就是用户请求的URL与views.py中函数的映射表。通过urls.py找到对应的函数
urlpatterns = [
    path('admin/', admin.site.urls),
    path('timer/', views.timer), #第一个是html文件的名称，第二个是视图函数名称，视图函数都在应用文件的views文件中
    path('login/', views.login, name='landing'),

    re_path(r'number/([0-9]{4})/$', views.change, name='change'),

    #路由配置
    #如果路径匹配中有匹配分组，则每个分组内容都是对应视图函数中的一个参数，有多少个分组对应的视图函数中就应该有多少个参数
    # re_path(r'^articles/2003/$', views.article_2003, name='a_2003'),
    # re_path(r'^articles/([0-9]{4})/$', views.articles_year, name='v_a_2005'),
    # re_path(r'^articles/([0-9]{4})/([0-9]{2})/$', views.articles_active),
    #re_path(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]{5})/$', views.articles_detials),

    #有名分组，将匹配分组命个名字，在views.py中匹配的对应属兔函数，中传的参数也必须是urls.py中有名分组的名称，这样在传参数时既可以不用管参数顺了
    #如果views.py中对应的视图函数参数名字和分组名字不一样，程序会报错
    # re_path(r'^articles/(?P<y>[0-9]{4})/(?P<m>[0-9]{2})/(?P<id>[0-9]{5})/$', views.articles_detials),
    path('article/<int:year>/<int:month>/',views.article_path),

    re_path('^index/$', views.index, name='index'),
    path('sel_url/<mm:month>', views.sel_url)

]













