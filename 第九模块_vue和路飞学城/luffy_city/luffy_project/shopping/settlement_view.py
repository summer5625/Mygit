# -*- coding: utf-8 -*-
# @Time    : 2019/11/29  18:30
# @Author  : XiaTian
# @File    : settlement_view.py

import redis
import json
from django.utils.timezone import now
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.BaseResponse import BaseResponse
from utils.redis_pool import POOL
from Course import models
from shopping import models
from utils.my_auth import LoginAuth


CONN = redis.Redis(connection_pool=POOL)
SHOPPINGCAR_KEY = 'SHOPPINGCAR_%s_%s'
SETTLEMENT_KEY = "SETTLEMENT_%s_%s"
GLOBAL_COUPON_KEY = "GLOBAL_COUPON_%s"


"""
加入结算中心的数据在redis中的存储结构

{
    settlement_user_id_course_id:{
        id, #课程id
        title，
        course_img,
        valid_period_display, # 课程所选价格的周期
        price,
        course_coupon_dict:{
            coupon_id: {}
            coupon_id2: {}
        }
         # 默认不给你选  这个字段只有更新的时候才添加
        default_course_coupon_id: 1  
    }
    
    global_coupon_userid: {
        coupon_id: {优惠券信息}
        coupon_id2: {优惠券信息}
        coupon_id3: {优惠券信息},
        # 这个字段只有更新的时候才添加
        default_global_coupon_id: 1
    
    }

}

"""


class SettlementView(APIView):
    authentication_classes = [LoginAuth]

    def post(self, request):
        res = BaseResponse()
        # 获取用户提交的课程id列表
        user_id = request.user.pk
        course_id_list = request.data.get('course_id_list', '')

        # 校验课程合法性
        for course_id in course_id_list:
            # 得到redis中存储的购物车课程的关键字
            shopping_car_key = SHOPPINGCAR_KEY % (user_id, course_id)
            if not CONN.exists(shopping_car_key):
                res.code = 1061
                res.error = '课程id不存在'

            # 构建redis数据结构
            # 获取用户所有的有效优惠券
            user_all_coupon = models.CouponRecord.objects.filter(
                account_id=user_id,
                status=0,
                coupon__valid_begin_date__lte=now(),
                coupon__valid_end_date__gte=now(),
            ).all()

            course_coupon_dict = {}
            globals_coupon_dict = {}

            for coupon_record in user_all_coupon:
                coupon = coupon_record.coupon
                
                if coupon.object_id == course_id:
                    course_coupon_dict[coupon.id] = {
                        "id": coupon.id,
                        "name": coupon.name,
                        "coupon_type": coupon.get_coupon_type_display(),
                        "object_id": coupon.object_id,
                        "money_equivalent_value": coupon.money_equivalent_value,
                        "off_percent": coupon.off_percent,
                        "minimum_consume": coupon.minimum_consume
                    }
                elif coupon.object_id == "":
                    globals_coupon_dict[coupon.id] = {
                        "id": coupon.id,
                        "name": coupon.name,
                        "coupon_type": coupon.get_coupon_type_display(),
                        "money_equivalent_value": coupon.money_equivalent_value,
                        "off_percent": coupon.off_percent,
                        "minimum_consume": coupon.minimum_consume
                    }

            course_info = CONN.hgetall(shopping_car_key)
            price_policy_dict = json.loads(course_info["price_policy_dict"])
            default_price_policy_id = course_info["default_price_policy_id"]
            valid_period = price_policy_dict[default_price_policy_id]["valid_period"]
            price = price_policy_dict[default_price_policy_id]["price"]
            
            settlement_info = {
                "id": course_info["id"],
                "title": course_info["title"],
                "course_img": course_info["course_img"],
                "valid_period": valid_period,
                "price": price,
                "course_coupon_dict": json.dumps(course_coupon_dict, ensure_ascii=False)
            }
            
            # 写入redis
            settlement_key = SETTLEMENT_KEY % (user_id, course_id)
            global_coupon_key = GLOBAL_COUPON_KEY % user_id
            CONN.hmset(settlement_key, settlement_info)
            if globals_coupon_dict:
                CONN.hmset(global_coupon_key, globals_coupon_dict)
                
            # 删除购物车中的数据
            CONN.delete(shopping_car_key)

        res.data = '加入结算中心成功'
        return Response(res.dict)

    def get(self, request):
        res = BaseResponse()
        user_id = request.user.pk
        settlement_key = SETTLEMENT_KEY % (user_id, "*")
        global_coupon_key = GLOBAL_COUPON_KEY % user_id

        all_keys = CONN.scan_iter(settlement_key)
        ret = []

        for key in all_keys:

            ret.append(CONN.hgetall(key))

        global_coupon_info = CONN.hgetall(global_coupon_key)

        res.data= {
            "settlement_info": ret,
            "global_coupon_info": global_coupon_info
        }

        return Response(res.dict)

    def put(self, request):
        res = BaseResponse()
        user_id = user_id = request.user.pk
        course_id = request.data.get('course_id', '')
        course_coupon_id = request.data.get('course_coupon_id', '')
        global_coupon_id = request.data.get('global_coupon_id', '') 
        
        # 校验课程合法性
        key = SETTLEMENT_KEY % (user_id, course_id)
        if course_id:
            if not CONN.exists(key):
                res.code = 1071
                res.error = '课程id不合法'
                return Response(res.dict)
        
        # 校验课程优惠券是否合法
        if course_coupon_id:
            course_coupon_dict = json.loads(CONN.hget(key, 'course_coupon_dict'))
            if str(course_coupon_id) not in course_coupon_dict:
                res.code = 1072
                res.error = '课程优惠券id不合法'
                return Response(res.dict)
            # 修改redis中数据
            CONN.hset(key, "default_course_coupon_id", course_coupon_id)

        # 校验全局优惠券是否合法
        if global_coupon_id:
            global_coupon_key = GLOBAL_COUPON_KEY % user_id
            if not CONN.exists(global_coupon_key):
                res.code = 1072
                res.error = '全局优惠券id不合法'
                return Response(res.dict)
            # 修改redis中数据
            CONN.hset(global_coupon_key, "default_global_coupon_id", global_coupon_id)
                
        res.data = '更新成功'
        return Response(res.dict)

    















