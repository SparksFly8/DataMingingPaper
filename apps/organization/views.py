from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

from .models import CourseOrg, CityDict
from .forms import UserAskForm

'''
课程机构列表View
'''
class OrgView(View):
    def get(self, request):
        # 查找到所有的课程机构
        all_orgs = CourseOrg.objects.all()
        # 热门机构,如果不加负号会是有小到大。
        hot_orgs = all_orgs.order_by('-click_nums')[:3]
        # 取出所有的城市
        all_cities = CityDict.objects.all()
        # 1.筛选-取出筛选城市(选择某个城市后，前端会传来值)
        city_id = request.GET.get('city', '')
        if city_id:   # 外键city在数据库中叫city_id
            all_orgs = all_orgs.filter(city_id=int(city_id))
        # 类别筛选
        category = request.GET.get('ct', '')
        if category:
            all_orgs = all_orgs.filter(category=category)
        # 进行排序
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                all_orgs = all_orgs.order_by('-students')
            elif sort == 'courses':
                all_orgs = all_orgs.order_by('-course_nums')
        # 总共有多少家机构使用count进行统计
        org_nums = all_orgs.count()
        # 2.分页-尝试获取页数参数
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
            'city_id':city_id,
            'category':category,
            'hot_orgs':hot_orgs,
            'sort':sort,
        })

'''
用户添加咨询(我要学习)
'''
class AddUserAskView(View):
    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            # 当commit为true进行真正保存
            user_ask = userask_form.save(commit=True)
            # 如果保存成功,返回json字符串,后面content type是告诉浏览器的
            return HttpResponse("{'status':'success'}", content_type='application/json')
        else:
            # 如果保存失败，返回json字符串,并将form的报错信息通过msg传递到前端
            return HttpResponse("{'status':'fail','msg':{0}}".format(userask_form.errors), content_type='application/json')
