from django.shortcuts import render
from django.contrib.auth import authenticate, login

# 当我们配置url被这个view处理时，自动传入request对象.
def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html', {})
    elif request.method == 'POST':
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
            return render(request, 'login.html', {})



