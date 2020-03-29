from django.db import models
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType


__all__ = ["Category", "Course", "CourseDetail", "Teacher", "DegreeCourse", "CourseChapter",
           "CourseSection", "PricePolicy", "OftenAskedQuestion", "Comment", "Account", "CourseOutline"]


# 课程分类表
class Category(models.Model):

    title = models.CharField(max_length=32, unique=True, verbose_name="课程的分类")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "课程分类表"
        db_table = verbose_name
        verbose_name_plural = verbose_name


# 课程表
class Course(models.Model):

    title = models.CharField(max_length=128, unique=True, verbose_name="课程的名称")
    # 存放课程图片的地址
    course_img = models.ImageField(upload_to="course/%Y-%m", verbose_name='课程的图片', null=True, blank=True)
    category = models.ForeignKey(to="Category", verbose_name="课程的分类", on_delete=None)

    COURSE_TYPE_CHOICES = ((0, "付费"), (1, "vip专享"), (2, "学位课程"))
    course_type = models.SmallIntegerField(choices=COURSE_TYPE_CHOICES)
    degree_course = models.ForeignKey(to="DegreeCourse", blank=True, null=True, help_text="如果是学位课程，必须关联学位表", on_delete=None)

    brief = models.CharField(verbose_name="课程简介", max_length=1024)
    level_choices = ((0, '初级'), (1, '中级'), (2, '高级'))
    level = models.SmallIntegerField(choices=level_choices, default=1)

    status_choices = ((0, '上线'), (1, '下线'), (2, '预上线'))
    status = models.SmallIntegerField(choices=status_choices, default=0)
    pub_date = models.DateField(verbose_name="发布日期", blank=True, null=True)

    order = models.IntegerField("课程顺序", help_text="从上一个课程数字往后排")
    study_num = models.IntegerField(verbose_name="学习人数", help_text="只要有人买课程，订单表加入数据的同时给这个字段+1")

    # 订单和优惠券
    # order_details = GenericRelation('OrderDetail', related_query_name="course")
    # coupon = GenericRelation('Coupon')
    
    # 只用于反向查询不生成字段，通过ContentType表关联
    price_policy = GenericRelation("PricePolicy") # 与价格策略表关联
    often_ask_questions = GenericRelation("OftenAskedQuestion") # 与常见问题表关联
    course_comments = GenericRelation("Comment") # 与评论表关联

    # 重新定义了更新和添加数据的保存方法，如果是学位课程则必须与学位课程表相关联，否则报错，保存不成功
    def save(self, *args, **kwargs):
        if self.course_type == 2:
            if not self.degree_course:
                raise ValueError("学位课必须关联学位课程表")
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "课程表"
        db_table = verbose_name
        verbose_name_plural = verbose_name


# 课程详细表
class CourseDetail(models.Model):

    # 与课程表一对一关联，课程表存放的是课程大致信息，这个信息时用户在网页上经常浏览的，查看频繁，如果将详情表的字段全部加到课程表
    # 用户在发送请求进行查询课程时，查找速度就会慢：表中字段越多查询速度就越慢
    course = models.OneToOneField(to="Course", on_delete=None)
    hours = models.IntegerField(verbose_name="课时", default=7)
    course_slogan = models.CharField(max_length=125, blank=True, null=True, verbose_name="课程口号")
    # 存放课程试跑资源链接
    video_brief_link = models.CharField(max_length=255, blank=True, null=True)
    summary = models.TextField(max_length=2048, verbose_name="课程概述")
    why_study = models.TextField(verbose_name="为什么学习这门课程")
    what_to_study_brief = models.TextField(verbose_name="我将学到哪些内容")
    career_improvement = models.TextField(verbose_name="此项目如何有助于我的职业生涯")
    prerequisite = models.TextField(verbose_name="课程先修要求", max_length=1024)
    # 推荐课程，与课程表多对多
    recommend_courses = models.ManyToManyField("Course", related_name="recommend_by", blank=True)

    teachers = models.ManyToManyField("Teacher", verbose_name="课程讲师")

    def __str__(self):
        return self.course.title

    class Meta:
        verbose_name = "课程详细表"
        db_table = verbose_name
        verbose_name_plural = verbose_name


# 讲师表
class Teacher(models.Model):

    name = models.CharField(max_length=32, verbose_name="讲师名字")
    brief = models.TextField(max_length=1024, verbose_name="讲师介绍")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "教师表"
        db_table = verbose_name
        verbose_name_plural = verbose_name


# 学位课程表
class DegreeCourse(models.Model):
    """
    字段大体跟课程表相同，哪些不同根据业务逻辑去区分
    """
    title = models.CharField(max_length=32, verbose_name="学位课程名字")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "学位课程表"
        db_table = verbose_name
        verbose_name_plural = verbose_name


# 课程章节表
class CourseChapter(models.Model):

    # 与课程表关联
    course = models.ForeignKey(to="Course", related_name="course_chapters", on_delete=None)
    # 用于进行章节排序
    chapter = models.SmallIntegerField(default=1, verbose_name="第几章")
    title = models.CharField(max_length=32, verbose_name="课程章节名称")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "课程章节表"
        db_table = verbose_name
        verbose_name_plural = verbose_name
        # 章节字段和课程字段联合唯一，即每个课程的摸个章节只能有一个
        unique_together = (["course", "chapter"])


# 课时表
class CourseSection(models.Model):

    # 与章节表关联，即某个章节课时是多少
    chapter = models.ForeignKey(to="CourseChapter", related_name="course_sections", on_delete=None)
    title = models.CharField(max_length=32, verbose_name="课时")
    # 进行课时排序用
    section_order = models.SmallIntegerField(verbose_name="课时排序", help_text="建议每个课时之间空1至2个值，以备后续插入课时")
    free_trail = models.BooleanField("是否可试看", default=False)

    section_type_choices = ((0, '文档'), (1, '练习'), (2, '视频'))
    section_type = models.SmallIntegerField(default=2, choices=section_type_choices)
    # 存放链接的
    section_link = models.CharField(max_length=255, blank=True, null=True, help_text="若是video，填vid,若是文档，填link")

    def course_chapter(self):
        return self.chapter.chapter

    def course_name(self):
        return self.chapter.course.title

    def __str__(self):
        return "%s-%s" % (self.chapter, self.title)

    class Meta:
        verbose_name = "课程课时表"
        db_table = verbose_name
        verbose_name_plural = verbose_name
        # 章节和章节对应的资源信息联合唯一
        unique_together = (['chapter', 'section_link'])


# 价格策略表
class PricePolicy(models.Model):

    # 与django中的ContentType表关联
    content_type = models.ForeignKey(to=ContentType, on_delete=None)  # 关联course or degree_course
    object_id = models.PositiveIntegerField()
    # 增删改查用，不生成字段
    content_object = GenericForeignKey('content_type', 'object_id')

    valid_period_choices = ((1, '1天'), (3, '3天'),
                            (7, '1周'), (14, '2周'),
                            (30, '1个月'),
                            (60, '2个月'),
                            (90, '3个月'),
                            (120, '4个月'),
                            (180, '6个月'), (210, '12个月'),
                            (540, '18个月'), (720, '24个月'),
                            (722, '24个月'), (723, '24个月'),
                            )
    valid_period = models.SmallIntegerField(choices=valid_period_choices, default=None)
    price = models.FloatField()

    def __str__(self):
        return "%s(%s)%s" % (self.content_object, self.get_valid_period_display(), self.price)

    class Meta:
        verbose_name = "价格策略表"
        db_table = verbose_name
        verbose_name_plural = verbose_name
        unique_together = (["content_type", 'object_id', "valid_period"])


# 常见问题
class OftenAskedQuestion(models.Model):

    content_type = models.ForeignKey(to=ContentType, on_delete=None)  # 关联course or degree_course
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    question = models.CharField(max_length=255)
    answer = models.TextField(max_length=1024)

    def __str__(self):
        return "%s-%s" % (self.content_object, self.question)

    class Meta:
        verbose_name = "常见问题表"
        db_table = verbose_name
        verbose_name_plural = verbose_name
        unique_together = (['content_type', 'object_id', 'question'])


# 通用的评论表
class Comment(models.Model):

    content_type = models.ForeignKey(to=ContentType, blank=True, null=True, on_delete=None) # 关联course or degree_course
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    content = models.TextField(max_length=1024, verbose_name="评论内容")
    account = models.ForeignKey("Account", verbose_name="会员名", on_delete=None)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "评价表"
        db_table = verbose_name
        verbose_name_plural = verbose_name


# 用户表
class Account(models.Model):

    username = models.CharField(max_length=32, verbose_name="用户姓名")
    pwd = models.CharField(max_length=32, verbose_name="密文密码")
    # head_img = models.CharField(max_length=256, default='/static/frontend/head_portrait/logo@2x.png',
    #                             verbose_name="个人头像")
    balance = models.IntegerField(verbose_name="贝里余额", default=0)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "用户表"
        db_table = verbose_name
        verbose_name_plural = verbose_name


# 课程大纲
class CourseOutline(models.Model):

    course_detail = models.ForeignKey(to="CourseDetail", related_name="course_outline", on_delete=None)
    title = models.CharField(max_length=128)
    order = models.PositiveSmallIntegerField(default=1)
    # 前端显示顺序

    content = models.TextField("内容", max_length=2048) # 换行也会存放，如果存放字符有换行，那么前端显示时也会换行

    def __str__(self):
        return "%s" % self.title

    class Meta:
        verbose_name = "课程大纲表"
        db_table = verbose_name
        verbose_name_plural = verbose_name
        unique_together = (['course_detail', 'title'])

