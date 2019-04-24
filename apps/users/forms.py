# encoding:utf-8
__author__ = 'shiliang'
__date__ = '2019/2/23 16:06'

from django import forms
# 引入验证码field
from captcha.fields import CaptchaField
from .models import UserProfile

'''
登录form
'''
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
    captcha = CaptchaField(error_messages={'invalid':'验证码错误'})

'''
找回密码form
'''
class ForgetPwdForm(forms.Form):
    # 此处email与前端name需保持一致
    email = forms.EmailField(required=True)
    # 应用验证码
    captcha = CaptchaField(error_messages={'invalid':'验证码错误'})

'''
重置密码form(点击邮件链接后的页面的form)
'''
class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)

class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['nick_name', 'gender', 'birthday', 'address', 'mobile']