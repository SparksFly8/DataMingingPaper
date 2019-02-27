# encoding:utf-8
__author__ = 'shiliang'
__date__ = '2019/2/27 16:45'

from django import forms
from operation.models import UserAsk
import re

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
    # 手机号的正则表达式验证
    def clean_mobile(self):
        moblie = self.cleaned_data['mobile']
        REGEX_MOBILE = '^1[358]\d{9}$|^147\d{8}$|^176\d{8}$'
        p = re.compile(REGEX_MOBILE)
        if p.match(moblie):
            return moblie
        else:
            raise forms.ValidationError('手机号码非法', code='mobile_invalid')

