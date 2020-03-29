# -*- coding: utf-8 -*-
# @Time    : 2019/11/8  18:22
# @Author  : XiaTian
# @File    : stark.py

from web import models
from stark.service.handle_table import site
from web.views.depart import DepartmentHandler
from web.views.school import SchoolHandler
from web.views.userinfo import UserInfoHandler
from web.views.course import CourseHandler
from web.views.class_list import ClassListHandler
from web.views.public_customer import PublicCustomerHandler
from web.views.private_customer import PrivateCustomerHandler
from web.views.consultant_record import ConsultantRecordHandler
from web.views.payment_record import PayRecordHandler
from web.views.check_payment_record import CheckPaymentHandler
from web.views.student import StudentHandler
from web.views.score_record import ScoreHandler
from web.views.course_record import ClassRecordHandler


site.register(models.School, SchoolHandler)
site.register(models.Department, DepartmentHandler)
site.register(models.UserInfo, UserInfoHandler)
site.register(models.Course, CourseHandler)
site.register(models.ClassList, ClassListHandler)
site.register(models.Customer, PrivateCustomerHandler, prev='private')
site.register(models.Customer, PublicCustomerHandler, prev='public')
site.register(models.ConsultRecord, ConsultantRecordHandler)
site.register(models.PaymentRecord, PayRecordHandler)
site.register(models.PaymentRecord, CheckPaymentHandler, prev='check')
site.register(models.Student, StudentHandler)
site.register(models.ScoreRecord, ScoreHandler)
site.register(models.CourseRecord, ClassRecordHandler)
