# encoding:utf-8
__author__ = 'shiliang'
__date__ = '2019/3/6 16:46'

from django.urls import path, include, re_path
from .views import affDistributeView

app_name = 'statistic'

urlpatterns = [
    # 课程机构列表url
    path('affDistribute/', affDistributeView.as_view(), name='affDistribute'),
]