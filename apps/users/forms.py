# encoding:utf-8
__author__ = 'shiliang'
__date__ = '2019/2/23 16:06'

from django import forms
# 引入验证码field
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)

'''
验证码form & 注册表单form
'''
class RegisterForm(forms.Form):
    # 此处email与前端name需保持一致
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=5)
    # 应用验证码
    captcha = CaptchaField()
