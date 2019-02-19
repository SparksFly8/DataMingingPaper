from django.db import models
from datetime import datetime

from django.contrib.auth.models import AbstractUser
'''
用户信息
'''
class UserProfile(AbstractUser):
    # 自定义的性别选择规则
    GENDER_CHOICES = (
        ('male',u'男'),
        ('female',u'女'),
    )
    # 昵称
    nick_name = models.CharField(max_length=50, verbose_name=u'昵称', default='')
    # 生日，可以为空
    birthday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    # 性别 只能男或女，默认男
    gender = models.CharField(
        max_length=5,
        verbose_name=u'性别',
        choices=GENDER_CHOICES,
        default='male'
    )
    # 地址
    address = models.CharField(max_length=100, verbose_name=u'地址', default='')
    # 电话
    mobile = models.CharField(max_length=11, verbose_name=u'电话', null=True, blank=True)
    # 头像 默认使用default.png
    image = models.ImageField(
        max_length=100,
        upload_to='image/%Y/%m',
        default=u'image/default.png'
    )
    # meta信息，即后台栏目名
    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name
    # 重载__str__方法，打印实例会打印username，username为继承自abstractuser
    def __str__(self):
        return self.username
'''
邮箱验证码
'''
class EmailVerifyRecord(models.Model):
    SEND_CHOICES = (
        ('register',u'注册'),
        ('forget',u'找回密码'),
    )
    code = models.CharField(max_length=20, verbose_name=u'验证码')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱')
    send_type = models.CharField(max_length=10, choices=SEND_CHOICES)
    # 这里的now得去掉(),不去掉会根据编译时间。而不是根据实例化时间。
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u'邮箱验证码'
        verbose_name_plural = verbose_name
'''
轮播图
'''
class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'标题')
    image = models.ImageField(
        max_length=100,
        verbose_name=u'轮播图',
        upload_to='banner/%Y/%m'
    )
    url = models.URLField(max_length=100, verbose_name=u'访问地址')
    # 默认index很大靠后。想要靠前修改index值。
    index = models.IntegerField(default=100, verbose_name=u'顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name