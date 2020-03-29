import uuid
import redis
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.BaseResponse import BaseResponse
from utils.redis_pool import POOL
from Course import models
from utils.my_auth import LoginAuth


"""
加入购物车：

    1、从前端拿到用户提交过来的数据
    
    2、解析前端拿过来的数据，并构造redis存储的数据格式
    {
        SHOPPINGCAR_USER_ID_COURSE_ID: {
        
            'id',
            'title',
            'course_img',
            'price_policy_dict': {
                price_policy_id1: '{valid_period, price}'
                price_policy_id2: '{valid_period, price}',
                price_policy_id3: '{valid_period, price}',
                
            },
            "default_price_policy_id"        
        } 
    }


"""

CONN = redis.Redis(connection_pool=POOL)
SHOPPINGCAR_KEY = 'SHOPPINGCAR_%s_%s'


class ShoppingCarView(APIView):
    authentication_classes = [LoginAuth]

    def post(self, request):

        res = BaseResponse()

        # 获取前端传过来的user_id和课程
        user_id = request.user.pk
        course_id = request.data.get('course_id', '')
        price_policy_id = request.data.get('price_policy_id', '')
        course_obj = models.Course.objects.filter(id=course_id).first()

        # 校验课程是否合法
        if not course_obj:
            res.code = 1051
            res.error = '课程不存在'
            return Response(res.dict)

        # 校验价格策略是否合法
        price_policy_queryset = course_obj.price_policy.all()
        price_policy_dict = {}
        for policy in price_policy_queryset:
            price_policy_dict[policy.id] = {
                "price": policy.price,
                "valid_period": policy.valid_period,
                "valid_period_display": policy.get_valid_period_display()
            }

        if price_policy_id not in price_policy_dict:
            res.code = 1052
            res.error = '价格策略不合法'
            return Response(res.dict)

        # 构建存到redis中的数据
        key = SHOPPINGCAR_KEY % (user_id, course_id)
        course_info = {
            "id": course_id,
            "title": course_obj.title,
            "course_img": str(course_obj.course_img),
            "price_policy_dict": json.dumps(price_policy_dict, ensure_ascii=False),
            "default_price_policy_id": price_policy_id
        }
        CONN.hmset(key, course_info)
        res.data = '加入购物车成功'

        return Response(res.dict)

    def get(self, request):

        res = BaseResponse()
        user_id = request.user.pk

        # *表示在redis中查找数据时是进行模糊匹配
        shopping_car_key = SHOPPINGCAR_KEY % (user_id, "*")

        # scan_iter在redis中进行模糊查询，返回的是一个生成器
        all_keys = CONN.scan_iter(shopping_car_key)

        ret = []

        for key in all_keys:
            ret.append(CONN.hgetall(key))
        res.data = ret

        return Response(res.dict)

    def put(self, request):
        res = BaseResponse()
        # 获取前端传来的用户id和课程id，和价格策略id
        user_id = request.user.pk
        course_id = request.data.get('course_id', '')
        price_policy_id = request.data.get('price_policy_id', '')
        key = SHOPPINGCAR_KEY % (user_id, course_id)

        # 判断课程是否合法
        if not CONN.exists(key):
            res.code = 1061
            res.error = '课程id不合法'
            return Response(res.dict)

        # 判断价格策略id是否合法
        price_policy_dict = json.loads(CONN.hget(key, 'price_policy_dict'))
        if str(price_policy_id) not in price_policy_dict:
            res.code = 1062
            res.error = '价格策略不合法'
            return Response(res.dict)

        # 修改数据
        CONN.hset(key, "default_price_policy_id", price_policy_id)
        res.data = '更新成功'

        return Response(res.dict)

    def delete(self, request):
        res = BaseResponse()

        user_id = request.user.pk
        course_id_list = request.data.get('course_id_list', '')

        for course_id in course_id_list:
            key = SHOPPINGCAR_KEY % (user_id, course_id)
            if not CONN.exists(key):
                res.code = 1061
                res.error = '课程id不合法'
                return Response(res.dict)
            CONN.delete(key)
        res.data = '删除成功'

        return Response(res.dict)
















