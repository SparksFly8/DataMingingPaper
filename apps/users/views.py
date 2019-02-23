from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from users.models import UserProfile
# 并集运算
from django.db.models import Q
# 基于类实现需要继承的view
from django.views.generic.base import View
from .forms import LoginForm, RegisterForm

# 实现用户名邮箱均可登录
# 继承ModelBackend类，因为它有方法authenticate，可点进源码查看
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # 不希望用户存在两个，get只能有一个。两个是get失败的一种原因 Q为使用并集查询
        try:
            # django的后台中密码加密：所以不能password==password
            # UserProfile继承的AbstractUser中有def check_password(self, raw_password):
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

'''
注册功能的view
'''
class RegisterView(View):
    def get(self, request):
        # 添加验证码
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form':register_form})
    def post(self, request):
        pass

class LoginView(View):
    # 直接调用get方法免去判断
    def get(self, request):
        # render三变量: request 模板名称 一个字典写明传给前端的值
        return render(request, 'login.html', {})
    def post(self, request):
        # 类实例化需要一个字典参数dict:request.POST就是一个QueryDict所以直接传入
        # POST中的usernamepassword，会对应到form中
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            # 成功返回user对象,失败返回null
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                # login_in 两参数：1.request, 2.user
                # 实际是对request写了一部分东西进去，然后在render的时候：
                # request是要render回去的。这些信息也就随着返回浏览器。完成登录
                login(request=request, user=user)
                return render(request, 'index.html', )
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误！'})
        else:
            return render(request, 'login.html', {'login_form': login_form})

