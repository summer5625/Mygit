# -*- coding: utf-8 -*-
# @Time    : 2019/11/27  14:50
# @Author  : XiaTian
# @File    : throttle.py
# 频率控制类
import time
from rest_framework.throttling import BaseThrottle, SimpleRateThrottle # 导入框架的频率限制类SimpleRateThrottle

VISIT_RECORD = {}


# 自定义频率限制类
# class MyThrottle(BaseThrottle):
#
#     def __init__(self):
#         self.history = None
#
#     def allow_request(self, request, view):
#         # 实现限流逻辑
#         # 以ip地址限流
#         # 访问列表{IP:[time1, time2 ....]}
#         """
#             限流逻辑：
#                 1、获取请求的IP地址
#                 2、判断ip是否在访问列表里面
#                     1.在访问列表里面，将当前的访问时间添加到对应的ip中
#                     2.不在访问列表里面，把当前访问的ip和时间添加到访问列表中
#                 3、确保列表中最老的访问时间和最新的访问时间差在1分钟内
#                 4、得到在访问的列表长度，判断是否是允许访问的次数
#         """
#
#         # 获取ip
#         ip = request.META.get('REMOTE_ADDR')
#
#         # 判断ip在不在访问列表中
#         now = time.time()
#         if ip not in VISIT_RECORD:
#             VISIT_RECORD[ip] = [now, ]
#             return True
#         # ip在列表里面添加上最新访问时间
#         history = VISIT_RECORD[ip]
#         history.insert(0, now)
#         while history[0] - history[-1] >60:
#             history.pop() # 删除最老的访问时间
#
#         self.history = history
#         if len(history) > 3:
#             return False
#         else:
#             return True
#
#     def wait(self):
#         # 返回等待的时间
#         wait_time = 60 - (self.history[0] - self.history[-1])
#         return wait_time


# 使用框架频率限制类
class MyThrottle(SimpleRateThrottle):
    # 必须要有scope
    scope = 'WD' # 与配置文件中配置的DEFAULT_THROTTLE_RATES字典中的key值对应
    
    # 必须要有get_cache_key方法
    def get_cache_key(self, request, view):

        # 获取当前ip
        key = self.get_ident(request)
        return key
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        