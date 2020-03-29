# -*- coding: utf-8 -*-
# @Time    : 2019/11/3  20:01
# @Author  : XiaTian
# @File    : stark.py


from app02.models import *
from stark.service.handle_table import site


site.register(Host)
site.register(Role)
