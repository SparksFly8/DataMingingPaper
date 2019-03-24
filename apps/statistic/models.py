from django.db import models

# Create your models here.
'''
机构国家分布
'''
class AffDistribute(models.Model):
    affiliation = models.CharField(max_length=220, verbose_name='机构名称')
    country = models.CharField(max_length=20, verbose_name=u'所属国家')
    count = models.IntegerField(default=0, verbose_name=u'发表频数')

    class Meta:
        # verbose_name_plural是verbose_name的复数形式。不设置则会自动补s。
        verbose_name = u'机构国家分布表'
        verbose_name_plural = verbose_name
    def __str__(self):
        return '{0}({1})'.format(self.affiliation, self.country)