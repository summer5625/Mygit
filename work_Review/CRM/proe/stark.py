# -*- coding: utf-8 -*-
# @Time    : 2020/2/14  13:35
# @Author  : XiaTian
# @File    : stark.py
from proe import models
from stark.service.handle_table import site
from proe.views.depart import DepartHandler
from proe.views.student import StudentHandler
from proe.views.school import SchoolHandler
from proe.views.class_list import ClassListHandler
from proe.views.course import CourseHandler
from proe.views.course_record import ClassRecordHandler
from proe.views.score_record import ScoreHandler
from proe.views.userinfo import UserHandler
from proe.views.check_payment_record import CheckPaymentHandler
from proe.views.consultant_record import ConsultantRecordHandler
from proe.views.payment_record import PayRecordHandler
from proe.views.private_customer import PrivateCustomerHandler
from proe.views.public_customer import PublicCustomerHandler


site.register(models.School, SchoolHandler)
site.register(models.Department, DepartHandler)
site.register(models.UserInfo, UserHandler)
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