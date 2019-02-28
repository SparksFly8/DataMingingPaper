from django.db import models
from datetime import datetime
'''
城市字典
'''
class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'城市')
    desc = models.CharField(max_length=200, verbose_name=u'描述')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'城市'
        verbose_name_plural = verbose_name
    def __str__(self):
        return '"{}"'.format(self.name)
'''
课程机构
'''
class CourseOrg(models.Model):
    CHOICES = (
        ('pxorg', '培训机构'),
        ('gx', '高校'),
        ('gr', '个人'),
    )
    name = models.CharField(max_length=50, verbose_name=u'机构名称')
    # 机构描述，后面会替换为富文本展示
    desc = models.TextField(verbose_name='机构描述', default='这个机构很懒，什么都没留下来')
    # 机构类别:
    category = models.CharField(max_length=20, verbose_name='机构类别', choices=CHOICES, default='pxorg')
    click_nums = models.IntegerField(default=0, verbose_name=u'点击量')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏数')
    image = models.ImageField(
        max_length=100,
        verbose_name=u'Logo',
        upload_to='org/%Y/%m'
    )
    address = models.CharField(max_length=150, verbose_name=u'机构地址')
    # 一个城市可以有很多课程机构，通过将city设置外键，变成课程机构的一个字段
    # 可以让我们通过机构找到城市
    city = models.ForeignKey('CityDict', verbose_name=u'所在城市', on_delete=models.CASCADE)
    students = models.IntegerField(default=0, verbose_name=u'学习人数')
    course_nums = models.IntegerField(default=0, verbose_name=u'课程数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程机构'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name
'''
讲师信息
'''
class Teacher(models.Model):
    # 一个机构会有很多老师，所以我们在讲师表添加外键并把课程机构名称保存下来
    # 可以使我们通过讲师找到对应的机构
    org = models.ForeignKey('CourseOrg', verbose_name=u'所属机构', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name=u'教师姓名')
    work_years = models.IntegerField(default=0, verbose_name=u'工作年限')
    work_company = models.CharField(max_length=50, verbose_name=u'就职公司')
    work_position = models.CharField(max_length=50, verbose_name=u'公司职位')
    points = models.CharField(max_length=50, default='无', verbose_name=u'教学特点')
    click_nums = models.IntegerField(default=0, verbose_name=u'点击量')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏数')
    image = models.ImageField(
        default='',
        upload_to="teacher/%Y/%m",
        verbose_name=u"头像",
        max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'教师'
        verbose_name_plural = verbose_name
    def __str__(self):
        return '{0}的教师{1}'.format(self.org, self.name)