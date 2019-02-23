# encoding:utf-8
__author__ = 'shiliang'
__date__ = '2019/2/23 16:06'

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
