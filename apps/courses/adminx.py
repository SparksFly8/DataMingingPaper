# encoding:utf-8
__author__ = 'shiliang'
__date__ = '2019/2/21 21:15'

import xadmin
from .models import Course, Lesson, Video, CourseResource

class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times',
                    'students', 'fav_nums', 'image', 'click_nums', 'add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'students', 'image']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times',
                    'students', 'fav_nums', 'image', 'click_nums', 'add_time']
class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    # __name代表使用外键中name字段
    list_filter = ['course__name', 'name', 'add_time']

class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    # __name代表使用外键中name字段
    list_filter = ['lesson__name', 'name', 'add_time']

class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name']
    # __name代表使用外键中name字段
    list_filter = ['course__name', 'name', 'download', 'add_time']

# 将管理器与model进行注册关联
xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
