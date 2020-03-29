# -*- coding: utf-8 -*-
# @Time    : 2019/11/29  23:36
# @Author  : XiaTian
# @File    : payment.py
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


CNN = redis.Redis(connection_pool=POOL)
SETTLEMENT_KEY = "SETTLEMENT_%s_%s"
GLOBAL_COUPON_KEY = "GLOBAL_COUPON_%s"


class PaymentView(APIView):
    authentication_classes = [LoginAuth]

    def post(self, request):
        res = BaseResponse()
        # 1、获取数据
        user_id = request.user.id
        balance = int(request.data.get('balance', 0))
        price = int(request.data.get('price', ''))  # 前端提交的打折后的价格
        # 2、校验数据是否合法
        # 2.1、校验贝里数是否合法
        if balance > request.user.balance:
            res.code = 1081
            res.error = '抵扣的贝里错误'
            return Response(res.dict)

        # 2.2、从用户的结算中心拿数据，与数据库存放数据比对
        settlement_key = SETTLEMENT_KEY % (user_id,'*')
        all_keys = CNN.scan_iter(settlement_key)
        course_total_price = 0
        for key in all_keys:
            settlement_info = CNN.hgetall(key)
            course_id = settlement_info['id']
            course_obj = models.Course.objects.filter(id=course_id).first()

            # 课程id是否合法
            if not course_obj and course_obj.status == 0:
                res.code = 1082
                res.error = '课程id不合法'
                return Response(res.dict)

            # 优惠券是否过期
            course_coupon_id = settlement_info.get('default_course_coupon_id', 0)
            course_coupon_dict = None

            if course_coupon_id:
                course_coupon_dict = models.Coupon.objects.filter(
                    id=course_coupon_id,
                    couponrecord__status=0,
                    couponrecord__account_id=user_id,
                    object_id = course_id,
                    valid_begin_date__lte=now(),
                    valid_end_date__gte=now(),
                ).values('coupon_type', 'money_equivalent_value', 'off_percent', 'minimum_consume')
            if not course_coupon_dict:
                res.code = 1083
                res.error = '课程优惠券不合法'
                return Response(res.dict)
            course_price = int(settlement_info['price'])
            course_rebate_price = self.account_price(course_coupon_dict, 0)
            if course_rebate_price == -1:
                res.code = 1085
                res.error = '课程优惠券不合法'
                return Response(res.dict)

            course_total_price += course_price

        # 校验全局优惠券
        global_coupon_key = GLOBAL_COUPON_KEY % user_id
        global_coupon_info = CNN.hgetall(global_coupon_key)
        global_coupon_id = int(global_coupon_info.get('default_global_coupon_id'))
        if global_coupon_id:
            global_coupon_dict = models.Coupon.objects.filter(
                id=global_coupon_id,
                couponrecord__status=0,
                couponrecord__account_id=user_id,
                valid_begin_date__lte=now(),
                valid_end_date__gte=now(),
            ).values('coupon_type', 'money_equivalent_value', 'off_percent', 'minimum_consume')

            if not global_coupon_dict:

                res.code = 1086
                res.error = '全局优惠券不合法'
                return Response(res.dict)

        course_rebate_price = self.account_price(global_coupon_dict, course_total_price)
        if course_rebate_price == -1:
            res.code = 1087
            res.error = '全局优惠券不合法'
            return Response(res.dict)
        course_total_price += course_rebate_price

        # 计算贝里折扣
        balance_money = balance / 100
        course_total_price -= balance_money

        # 2.3、校验价格是否合法
        if price != course_total_price:
            res.code = 1088
            res.error = '价格不合法'
            return Response(res.dict)
        # 3、调用支付接口支付
        # 4、支付成功后修改数据库中用户信息
        res.data = '支付成功'

        return Response(res.dict)

    def account_price(self, coupon_dict, price):

        coupon_type = coupon_dict['coupon_type']

        if coupon_type == 0:
            money_equivalent_value = coupon_dict['money_equivalent_value']
            if price - money_equivalent_value >= 0:
                rebate_price = price - money_equivalent_value
            else:
                rebate_price = 0

        elif coupon_type == 1:
            money_equivalent_value = coupon_dict['money_equivalent_value']
            minimum_consume = coupon_dict['minimum_consume']
            if price >= minimum_consume:
                rebate_price  = price - money_equivalent_value
            else:
                rebate_price = -1

        elif coupon_type == 2:
            off_percent = coupon_dict['off_percent']
            minimum_consume = coupon_dict['minimum_consume']

            if price >= minimum_consume:
                rebate_price  = price * (off_percent / 100)
            else:
                rebate_price = -1

        return rebate_price

