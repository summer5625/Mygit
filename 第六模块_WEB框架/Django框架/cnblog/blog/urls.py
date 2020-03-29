"""cnblog URL Configuration

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
from django.urls import path, re_path


from blog import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('get_valid_img/', views.get_valid_img),
    path('index/', views.index),
    path('reg/', views.register),
    path('logout/', views.logout),
    path('comments/', views.comments),
    path('comment_tree/', views.get_comment_tree),
    path('backend/', views.backend),
    path('add_article/', views.add_article),
    path('upload/', views.upload),
    
    # 文章点赞
    path('digg/', views.digg),

    # 个人站点url
    re_path(r'^(?P<username>\w+)$', views.home_site),

    # 个人站点文章分类跳转
    re_path(r'^(?P<username>\w+)/(?P<condition>tag|category|archive)/(?P<param>.*)/$', views.home_site),
    
    # 文章详情
    re_path(r'^(?P<username>\w+)/articles/(?P<article_id>.*)', views.article_details),

    # 删除文章
    re_path(r'^(?P<username>\w+)/delete/(?P<article_id>.*)', views.delete_article),
    
    # 修改文章
    re_path(r'^(?P<username>\w+)/change/(?P<article_id>.*)', views.change_article),

]
