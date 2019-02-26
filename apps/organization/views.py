from django.shortcuts import render
from django.views.generic import View
from organization.models import CourseOrg, CityDict

'''
课程机构列表View
'''
class OrgView(View):
    def get(self, request):
        # 查找到所有的课程机构
        all_orgs = CourseOrg.objects.all()
        org_nums = CourseOrg.objects.count()
        # 取出所有的城市
        all_cities = CityDict.objects.all()
        return render(request, 'org-list.html', {
            'all_orgs':all_orgs,
            'all_cities':all_cities,
            'org_nums':org_nums,
        })