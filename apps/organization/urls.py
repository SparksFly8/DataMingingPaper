# encoding:utf-8
__author__ = 'shiliang'
__date__ = '2019/2/27 16:57'

from django.urls import path, include, re_path
from organization.views import OrgView, AddUserAskView

app_name = 'organization'

urlpatterns = [
    # 课程机构列表url
    path('list/', OrgView.as_view(), name='org_list'),
    path('add_ask/', AddUserAskView.as_view(), name='add_ask'),
]