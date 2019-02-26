# encoding:utf-8
__author__ = 'shiliang'
__date__ = '2019/2/21 22:26'

import xadmin
from .models import CityDict, CourseOrg, Teacher

# 机构所属城市名后台管理器
class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']

# 机构课程信息管理器
class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'fav_nums']
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city']
    # __name代表使用外键中name字段
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums',
                    'image', 'address', 'city__name', 'add_time']

# 讲师信息管理器
class TeacherAdmin(object):
    list_display = ['name', 'org', 'work_years', 'work_company','work_position',
                    'points', 'click_nums', 'fav_nums', 'add_time']
    search_fields = ['org', 'name', 'work_company', 'work_position']
    # __name代表使用外键中name字段
    list_filter = ['org__name', 'name', 'work_years', 'work_company',
                    'work_position', 'points', 'click_nums', 'fav_nums', 'add_time']

xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)