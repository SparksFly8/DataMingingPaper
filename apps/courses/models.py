from django.db import models
from datetime import datetime
'''
1.课程信息表
'''
class Course(models.Model):
    DEGREE_CHOICES = (
        ('cj',u'初级'),
        ('zj',u'中级'),
        ('gj',u'高级'),
    )
    name = models.CharField(max_length=50, verbose_name=u'课程名称')
    desc = models.CharField(max_length=300, verbose_name=u'课程描述')
    # TextField允许我们不输入长度。可以输入到无限大。暂时定义为TextFiled，之后更新为富文本
    detail = models.TextField(verbose_name=u'课程详情')
    degree = models.CharField(max_length=2, choices=DEGREE_CHOICES)
    learn_times = models.IntegerField(default=0, verbose_name=u'学习时长')
    students = models.IntegerField(default=0, verbose_name=u'学习人数')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏人数')
    image = models.ImageField(
        max_length=100,
        verbose_name=u'封面图',
        upload_to='courses/%Y/%m'
    )
    click_nums = models.IntegerField(default=0, verbose_name=u'点击量')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程'
        verbose_name_plural = verbose_name
'''
2.章节
'''
class Lesson(models.Model):
    # 因为一个课程对应很多章节。所以在章节表中将课程设置为外键。
    # 作为一个字段来让我们可以知道这个章节对应那个课程
    # Django2.1版本的ForeignKey()中必须要加on_delete参数;CASCADE表示级联删除;
    # 2.1版本语法: models.ForeignKey('self', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', verbose_name=u'课程', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u'章节名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'章节'
        verbose_name_plural = verbose_name
'''
3.每章视频
'''
class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u'章节', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u'视频名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'视频'
        verbose_name_plural = verbose_name
'''
4.课程资源
'''
class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'课程', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u'资源名称')
    download = models.FileField(
        max_length=100,
        verbose_name=u'资源文件',
        upload_to='course/resource/%Y/%m'
    )
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程资源'
        verbose_name_plural = verbose_name