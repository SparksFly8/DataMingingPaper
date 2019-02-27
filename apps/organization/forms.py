# encoding:utf-8
__author__ = 'shiliang'
__date__ = '2019/2/27 16:45'

from django import forms
from operation.models import UserAsk

'''
进阶版本的modelform：它可以向model一样save
'''
class UserAskForm(forms.ModelForm):
    # 继承之余还可以新增字段
    # 是由哪个model转换的
    class Meta:
        model = UserAsk
        # 需要验证的字段
        fields = ['name', 'mobile', 'course_name']