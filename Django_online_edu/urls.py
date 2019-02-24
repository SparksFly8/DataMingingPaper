"""Django_online_edu URL Configuration

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
# 导入xadmin，替换admin
import xadmin
from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    # TemplateView.as_view会将template转换为view
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('captcha/', include('captcha.urls')),
    # 这里的'P'是参数(parameter)的意思;'.*'代表全部提取的正则
    re_path('active/(?P<active_code>.*)/', ActiveUserView.as_view(), name='user_active'),
    re_path('reset/(?P<reset_code>.*)/', ResetView.as_view(), name='reset_pwd'),
    path('forgetPwd/', ForgetPwdView.as_view(), name='forget_pwd'),
    path('modifyPwd/', ModifyPwdView.as_view(), name='modify_pwd'),
]
