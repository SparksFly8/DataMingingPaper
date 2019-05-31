"""DataMingingPaper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.static import serve
# 导入xadmin，替换admin
import xadmin
from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView, LogoutView
from DataMingingPaper.settings import MEDIA_ROOT, STATIC_ROOT


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    # TemplateView.as_view会将template转换为view
    path('', TemplateView.as_view(template_name='homepage.html'), name='homepage'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('captcha/', include('captcha.urls')),
    # 这里的'P'是参数(parameter)的意思;'.*'代表全部提取的正则
    re_path('active/(?P<active_code>.*)/', ActiveUserView.as_view(), name='user_active'),
    re_path('reset/(?P<reset_code>.*)/', ResetView.as_view(), name='reset_pwd'),
    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path('media/(?P<path>.*)', serve, {'document_root':MEDIA_ROOT}),
    re_path('static/(?P<path>.*)', serve, {'document_root':STATIC_ROOT}),


    path('forgetPwd/', ForgetPwdView.as_view(), name='forget_pwd'),
    path('modifyPwd/', ModifyPwdView.as_view(), name='modify_pwd'),

    # 论文统计app
    path('statistic/', include('statistic.urls', namespace='statistic')),

    # 用户信息app
    path('user/', include('users.urls', namespace='users')),
]
