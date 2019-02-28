# encoding:utf-8
__author__ = 'shiliang'
__date__ = '2019/2/27 16:57'

from django.urls import path, include, re_path
from organization.views import OrgView, AddUserAskView, OrgHomeView, OrgCourseView, OrgDescView, OrgTeacherView

app_name = 'organization'

urlpatterns = [
    # 课程机构列表url
    path('list/', OrgView.as_view(), name='org_list'),
    path('add_ask/', AddUserAskView.as_view(), name='add_ask'),
    # home页面,取纯数字
    re_path('home/(?P<org_id>\d+)/', OrgHomeView.as_view(), name='org_home'),
    re_path('course/(?P<org_id>\d+)/', OrgCourseView.as_view(), name='org_course'),
    re_path('desc/(?P<org_id>\d+)/', OrgDescView.as_view(), name='org_desc'),
    re_path('teacher/(?P<org_id>\d+)/', OrgTeacherView.as_view(), name='org_teacher'),
]