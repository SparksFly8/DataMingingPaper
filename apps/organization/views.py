from django.shortcuts import render
from django.views.generic import View
from organization.models import CourseOrg, CityDict
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

'''
课程机构列表View
'''
class OrgView(View):
    def get(self, request):
        # 查找到所有的课程机构
        all_orgs = CourseOrg.objects.all()
        # 总共有多少家机构使用count进行统计
        org_nums = CourseOrg.objects.count()
        # 取出所有的城市
        all_cities = CityDict.objects.all()
        # 尝试获取页数参数
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1    # 如果是不合法的配置参数默认返回第一页
        # 对于取到的数据进行分页处理,这里指从all_orgs中取per_page个出来。
        p = Paginator(all_orgs, per_page=4, request=request)
        # 此时前台显示的就应该是我们此时获取的第几页的数据
        orgs = p.page(page)

        return render(request, 'org-list.html', {
            'all_orgs':orgs,
            'all_cities':all_cities,
            'org_nums':org_nums,
        })