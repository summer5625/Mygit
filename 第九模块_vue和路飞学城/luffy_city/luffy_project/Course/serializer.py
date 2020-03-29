# -*- coding: utf-8 -*-
# @Time    : 2019/11/28  15:49
# @Author  : XiaTian
# @File    : serializer.py

from rest_framework import serializers
from Course import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    level = serializers.CharField(source='get_level_display')
    price = serializers.SerializerMethodField()

    def get_price(self, obj):
        return obj.price_policy.all().order_by('price').first().price

    class Meta:
        model = models.Course
        fields = ['id', 'title', 'course_img', 'brief', 'level', 'study_num', 'price']


class CourseDetailSerializer(serializers.ModelSerializer):
    level = serializers.CharField(source='course.get_level_display')
    study_num = serializers.IntegerField(source='course.study_num')
    recommend_courses = serializers.SerializerMethodField()
    teachers = serializers.SerializerMethodField()
    price_policy = serializers.SerializerMethodField()
    course_outline = serializers.SerializerMethodField()

    def get_course_outline(self, obj):
        return [{'id': outline.id, 'title': outline.title, 'content': outline.content} for outline in
                obj.course_outline.all().order_by('order')]

    def get_price_policy(self, obj):
        return [{'id': price.id, 'valid_period_display': price.get_valid_period_display(), 'price': price.price} for
                price in obj.course.price_policy.all()]

    def get_teachers(self, obj):
        return [{'id': teacher.id, 'name': teacher.name, 'teacher_brief': teacher.brief} for teacher in
                obj.teachers.all()]

    def get_recommend_courses(self, obj):
        return [{'id': course.id, 'title': course.title} for course in obj.recommend_courses.all()]

    class Meta:
        model = models.CourseDetail
        fields = ['id', 'hours', 'summary', 'level', 'study_num', 'why_study', 'what_to_study_brief',
                  'career_improvement', 'prerequisite', 'recommend_courses', 'teachers', 'price_policy',
                  'course_outline']


class CourseChapterSerializer(serializers.ModelSerializer):
    sections = serializers.SerializerMethodField()
    
    def get_sections(self, obj):
        
        return [{'id': section.id, 'title': section.title, 'free_trail': section.free_trail} for section in obj.course_sections.all().order_by('section_order')]
    
    class Meta:
        
        model = models.CourseChapter
        fields = ['id', 'title', 'sections']


class CourseCommentSerializer(serializers.ModelSerializer):

    account = serializers.CharField(source='account.username')

    class Meta:

        model = models.Comment
        fields = ['id', 'content', 'account', 'date']


class CourseQuestionSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.OftenAskedQuestion
        fields = ['id', 'question', 'answer']














