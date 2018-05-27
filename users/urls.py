'''为应用程序 users 定义 URL 模式'''

from django.conf.urls import url
from django.contrib.auth.views import login # 默认视图

from . import views

urlpatterns = [
    # 登录页面
    url(r'^login/$',login,{'template_name':'users/login.html'},name='login'),
    url(r'^logout/$',views.logout_view,name='logout'),
    # 注册页面
    url(r'^register/$',views.register,name='register'),
]
