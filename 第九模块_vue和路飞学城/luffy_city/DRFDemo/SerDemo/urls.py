"""DRFDemo URL Configuration

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
from django.urls import path
from SerDemo import views

# DRF路由组件：不用再写很多路由
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"", views.BookModelViewSet) # r""是路由的匹配规则，但是不能加截止符$,

urlpatterns = [
    # path('list/', views.BookView.as_view()),
    # path('retrieve/<int:id>', views.BookEditView.as_view()),
    # path('list/', views.BookModelViewSet.as_view({'get': 'list', 'post': 'create'})),
    # path('retrieve/<int:id>', views.BookModelViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    # 继承了框架提供的ModelViewSet类，id必须改为pk
    # path('retrieve/<int:pk>', views.BookModelViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]

urlpatterns += router.urls


"""
注意使用DRF路由组件时要慎重，因为DRF路由组件自动生成的路由都带参数的路由，会暴露很多保密信息

"""