from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from ContentTypeDemo import models


class ContentTypeView(APIView):
    
    def get(self, request):

        # Food:12
        # Fruit:13
        # Coupon:11

        # 给面包创建优惠券
        food_obj = models.Food.objects.filter(id=1).first()
        # models.Coupon.objects.create(title='面包八折', content_type_id=12, object_id=1)
        # models.Coupon.objects.create(title='面包五折优惠', content_obj=food_obj)

        # 查询面包有哪些优惠券
        coupons = food_obj.coupons.all()
        # print(coupons)
        
        # 通过优惠券查属于哪个对象
        coupon_obj = models.Coupon.objects.filter(id=1).first()
        content_obj = coupon_obj.content_obj
        # print(content_obj)

        # 通过ContentType表，查找对应的表模型
        content = models.ContentType.objects.filter(app_label='ContentTypeDemo', model='food').first()
        # print(content)
        model_class = content.model_class() # 拿到表模型，可以对拿到的表进行操作
        ret = model_class.objects.all()
        print(ret)

        return Response('content_type测试')
