from django.db import models

from rbac.models import UserInfo as RbacUserInfo


# 校区表
class School(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='校区', max_length=32)

    def __str__(self):
        return self.title


# 部门表
class Department(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='部门', max_length=32)

    def __str__(self):
        return self.title


# 用户表
class UserInfo(RbacUserInfo):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(verbose_name='姓名', max_length=32)
    gender_choices = ((1, '男'), (2, '女'))
    gender = models.IntegerField(
        verbose_name='性别',
        choices=gender_choices,
        default=1)
    password = models.CharField(verbose_name='密码', max_length=64)
    email = models.CharField(verbose_name='邮箱', max_length=32)
    depart = models.ForeignKey(
        verbose_name='部门',
        to='Department',
        on_delete=models.CASCADE)
    phone = models.CharField(verbose_name='电话', max_length=32, unique=True)

    def __str__(self):
        return self.nickname


# 课程表
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='课程', max_length=32, unique=True)

    def __str__(self):
        return self.title


# 班级表
class ClassList(models.Model):
    id = models.AutoField(primary_key=True)
    school = models.ForeignKey(
        verbose_name='校区',
        to='School',
        on_delete=models.CASCADE)
    course = models.ForeignKey(
        verbose_name='课程',
        to='Course',
        on_delete=models.CASCADE)
    semester = models.PositiveIntegerField(verbose_name='班级(期)')  # 正整数
    price = models.IntegerField(verbose_name='学费')
    start_date = models.DateField(verbose_name='开班日期')
    graduate_date = models.DateField(
        verbose_name='结业日期', null=True, blank=True)

    # limit_choices_to用于限制关联的字段筛选，页面展示时只展示筛选的特定对象,方便页面表单展示
    class_teacher = models.ForeignKey(
        verbose_name='班主任',
        to=UserInfo,
        limit_choices_to={
            'depart__title': '教质部'},
        related_name='classes',
        on_delete=models.CASCADE)
    tec_teacher = models.ManyToManyField(
        verbose_name='任课老师',
        to='UserInfo',
        limit_choices_to={
            'depart__title__in': [
                'Linux教学部',
                'python教学部']},
        related_name='teach_teacher',
        blank=True)
    memo = models.TextField(verbose_name='说明', null=True, blank=True)

    def __str__(self):
        return '{0}({1}期)'.format(self.course.title, self.semester)


# 客户表
class Customer(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='姓名', max_length=32)
    contact = models.CharField(
        verbose_name='联系方式',
        max_length=64,
        unique=True,
        help_text='QQ/微信/手机号')
    status_choices = [
        (1, "已报名"),
        (2, "未报名")
    ]
    status = models.IntegerField(
        verbose_name='状态',
        choices=status_choices,
        default=2)
    gender_choices = ((1, '男'), (2, '女'))
    gender = models.SmallIntegerField(
        verbose_name='性别',
        choices=gender_choices,
        default=1)
    source_choices = [
        (1, "qq群"),
        (2, "内部转介绍"),
        (3, "官方网站"),
        (4, "百度推广"),
        (5, "360推广"),
        (6, "搜狗推广"),
        (7, "腾讯课堂"),
        (8, "广点通"),
        (9, "高校宣讲"),
        (10, "渠道代理"),
        (11, "51cto"),
        (12, "智汇推"),
        (13, "网盟"),
        (14, "DSP"),
        (15, "SEO"),
        (16, "其它"),
    ]

    source = models.SmallIntegerField(
        verbose_name='客户来源',
        choices=source_choices,
        default=1)

    referral_from = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        verbose_name='学员转介绍',
        help_text='若此客户是转介绍自内部学员,请在此处选择内部学员姓名',
        related_name="internal_referral",
        on_delete=models.CASCADE
    )

    course = models.ManyToManyField(verbose_name='咨询课程', to='Course')
    consultant = models.ForeignKey(
        verbose_name='课程顾问',
        to='UserInfo',
        limit_choices_to={
            'depart__title': '销售部'},
        related_name='consultant',
        null=True,
        blank=True,
        on_delete=models.CASCADE)

    education_choices = (
        (1, '重点大学'),
        (2, '普通本科'),
        (3, '独立院校'),
        (4, '民办本科'),
        (5, '大专'),
        (6, '民办专科'),
        (7, '高中'),
        (8, '其他')
    )
    education = models.SmallIntegerField(
        verbose_name='学历',
        choices=education_choices,
        null=True,
        blank=True)
    graduation_school = models.CharField(
        verbose_name='毕业学校', max_length=64, null=True, blank=True)
    major = models.CharField(
        verbose_name='所学专业',
        max_length=64,
        null=True,
        blank=True)

    experience_choices = [
        (1, '在校生'),
        (2, '应届毕业'),
        (3, '半年以内'),
        (4, '半年至一年'),
        (5, '一年至三年'),
        (6, '三年至五年'),
        (7, '五年以上'),
    ]
    experience = models.IntegerField(
        verbose_name='工作经验',
        choices=experience_choices,
        blank=True,
        null=True)
    work_status_choices = [
        (1, '在职'),
        (2, '无业')
    ]
    work_status = models.IntegerField(
        verbose_name='职业状态',
        choices=work_status_choices,
        default=1,
        blank=True,
        null=True)
    company = models.CharField(
        verbose_name='就职公司',
        max_length=64,
        blank=True,
        null=True)
    salary = models.CharField(
        verbose_name="当前薪资",
        max_length=64,
        blank=True,
        null=True)
    date = models.DateField(verbose_name="咨询日期", auto_now_add=True)
    last_consult_date = models.DateField(
        verbose_name="最后跟进日期", auto_now_add=True)

    def __str__(self):
        return self.name


# 客户跟进记录
class ConsultRecord(models.Model):

    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(verbose_name='咨询客户', to='Customer', on_delete=models.CASCADE)
    consultant = models.ForeignKey(verbose_name='跟进人', to='UserInfo', on_delete=models.CASCADE)
    note = models.TextField(verbose_name='跟进内容')
    date = models.DateField(verbose_name='跟进日期', auto_now_add=True)


# 缴费申请表
class PaymentRecord(models.Model):

    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(verbose_name='客户', to='Customer', on_delete=models.CASCADE)
    consultant= models.ForeignKey(verbose_name='课程顾问', to='UserInfo', help_text='谁签的单，就选谁', on_delete=models.CASCADE)
    pay_type_choices = [
        (1, "报名费"),
        (2, "学费"),
        (3, "退学"),
        (4, "其他"),
    ]
    pay_type = models.IntegerField(verbose_name='费用类型', choices=pay_type_choices, default=1)
    paid_fee =models.IntegerField(verbose_name='金额', default=0)
    class_list = models.ForeignKey(verbose_name='申请班级', to='ClassList', on_delete=models.CASCADE)
    apply_date = models.DateTimeField(verbose_name='申请日期', auto_now_add=True)
    confirm_status_choices = (
        (1, '申请中'),
        (2, '已确认'),
        (3, '已驳回'),
    )
    confirm_status = models.IntegerField(verbose_name='确认状态', choices=confirm_status_choices, default=1)
    confirm_date = models.DateTimeField(verbose_name='确认日期', null=True, blank=True)
    confirm_user = models.ForeignKey(verbose_name='审批人', to='UserInfo', related_name='confirms', null=True, blank=True, on_delete=models.CASCADE)
    note = models.TextField(verbose_name='备注', null=True, blank=True)


# 学生表
class Student(models.Model):

    id = models.AutoField(primary_key=True)
    customer = models.OneToOneField(verbose_name='客户信息', to='Customer', on_delete=models.CASCADE)
    qq = models.CharField(verbose_name='QQ号', max_length=32)
    mobile = models.CharField(verbose_name='电话', max_length=32)
    emergency_contract =models.CharField(verbose_name='紧急联系人', max_length=32)
    class_list = models.ManyToManyField(verbose_name='已报班级', to='ClassList', blank=True)
    student_status_choices = [
        (1, "申请中"),
        (2, "在读"),
        (3, "毕业"),
        (4, "退学")
    ]
    student_status = models.IntegerField(verbose_name='学员状态', choices=student_status_choices, default=1)
    score = models.IntegerField(verbose_name='积分', default=100)
    memo =models.TextField(verbose_name='备注', max_length=255, blank=True, null=True)

    def __str__(self):
        return self.customer.name


# 积分记录
class ScoreRecord(models.Model):

    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(verbose_name='学生', to='Student', on_delete=models.CASCADE)
    content = models.TextField(verbose_name='理由')
    score = models.IntegerField(verbose_name='分值', help_text='违纪扣分写负值，表现邮寄加分写正值')
    user = models.ForeignKey(verbose_name='执行人', to='UserInfo', on_delete=models.CASCADE)


#  上课记录表
class CourseRecord(models.Model):

    id = models.AutoField(primary_key=True)
    class_object = models.ForeignKey(verbose_name="班级", to="ClassList", on_delete=models.CASCADE)
    day_num = models.IntegerField(verbose_name="节次")
    teacher = models.ForeignKey(verbose_name="讲师", to='UserInfo', limit_choices_to={'depart__title__in': [
        'Linux教学部', 'python教学部']}, on_delete=models.CASCADE)
    date = models.DateField(verbose_name="上课日期", auto_now_add=True)

    def __str__(self):
        return "{0} day{1}".format(self.class_object, self.day_num)


# 学生考勤记录
class StudyRecord(models.Model):

    id = models.AutoField(primary_key=True)
    course_record = models.ForeignKey(verbose_name="第几天课程", to="CourseRecord", on_delete=models.CASCADE)
    student = models.ForeignKey(verbose_name="学员", to='Student', on_delete=models.CASCADE)
    record_choices = (
        ('checked', "已签到"),
        ('vacate', "请假"),
        ('late', "迟到"),
        ('noshow', "缺勤"),
        ('leave_early', "早退"),
    )
    record = models.CharField("上课纪录", choices=record_choices, default="checked", max_length=64)



















