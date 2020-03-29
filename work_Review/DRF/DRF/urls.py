"""DRF URL Configuration

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
from django.urls import path, include
from demon.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('version/', include('version.urls')),
    path('auth/', include('authView.urls')),
    path('page/', include('pageView.urls')),
    path('parser/', include('parseView.urls')),
    path('course/', include('coruseView.urls')),
    # path('get/', BookView.as_view()),
    # path('edit/<int:id>', BookEditView.as_view()),
    path('get/', BookModelViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('edit/<int:id>', BookModelViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'distroy'}))
]
