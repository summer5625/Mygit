from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


from Course import models
from Course import serializer


class CategoryView(APIView):
    
    def get(self, request):
        queryset = models.Category.objects.all()
        ser_obj = serializer.CategorySerializer(queryset, many=True)
        return Response(ser_obj.data)


class CourseView(APIView):
    
    def get(self, request):
        
        # 拿到分类id
        category_id = request.query_params.get('category', 0)
        
        # 判断分类id是否是0，是0返回所有课程
        if category_id == 0:
            queryset = models.Course.objects.all().order_by('order')
        else:
            queryset = models.Course.objects.filter(category_id=category_id).order_by('order')
        ser_obj = serializer.CourseSerializer(queryset, many=True)

        return Response(ser_obj.data)
    
    
class CourseDetailView(APIView):
    
    def get(self, request, pk):

        course_detail_obj = models.CourseDetail.objects.filter(course__id=pk).first()

        if not course_detail_obj:
            return Response({'code': 1001, 'error': '查询的课程不存在'})

        ser_obj = serializer.CourseDetailSerializer(course_detail_obj)
        
        return Response(ser_obj.data)


class CourseChapterView(APIView):
    
    def get(self, request, pk):

        queryset = models.CourseChapter.objects.filter(course_id=pk).all().order_by('chapter')

        ser_obj = serializer.CourseChapterSerializer(queryset, many=True)
        
        return Response(ser_obj.data)
        

class CourseCommentView(APIView):
    
    def get(self, request, pk):
        queryset = models.Course.objects.filter(id=pk).first().course_comments.all()

        ser_obj = serializer.CourseCommentSerializer(queryset, many=True)
        
        return Response(ser_obj.data)
    
    
class CourseQuestionView(APIView):
    
    def get(self, request, pk):
        queryset = models.Course.objects.filter(id=pk).first().often_ask_questions.all()
        ser_obj = serializer.CourseQuestionSerializer(queryset, many=True)
        return Response(ser_obj.data)
        
        

        

        

        
        
        
        
        
        
    