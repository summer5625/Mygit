# -*- coding: utf-8 -*-
# @Time    : 2019/11/28  15:40
# @Author  : XiaTian
# @File    : urls.py
from django.urls import path
from Course import views


urlpatterns = [
    path('category/', views.CategoryView.as_view()),
    path('list', views.CourseView.as_view()),
    path('detail/<int:pk>', views.CourseDetailView.as_view()),
    path('chapter/<int:pk>', views.CourseChapterView.as_view()),
    path('comment/<int:pk>', views.CourseCommentView.as_view()),
    path('question/<int:pk>', views.CourseQuestionView.as_view()),
]
