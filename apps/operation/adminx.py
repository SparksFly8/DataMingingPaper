# encoding:utf-8
__author__ = 'shiliang'
__date__ = '2019/2/21 21:58'

import xadmin
from .models import UserAsk, CourseComments, UserFavorite, UserMessage, UserCourse

# 用户表单我要学习后台管理器
class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']

# 用户评论后台管理器
class CourseCommentsAdmin(object):
    list_display = ['user', 'course', 'comments', 'add_time']
    search_fields = ['user', 'course', 'comments']
    list_filter = ['user', 'course', 'comments', 'add_time']

# 用户收藏后台管理器
class UserFavoriteAdmain(object):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']

# 用户消息后台管理器
class UserMessageAdmin(object):
    list_display = ['user', 'message', 'is_read', 'add_time']
    search_fields = ['user', 'message', 'is_read']
    list_filter = ['user', 'message', 'is_read', 'add_time']

# 用户课程学习后台管理器
class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']

# 将后台管理器与models进行关联注册。
xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmain)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)