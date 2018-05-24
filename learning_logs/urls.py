'''定义 learning_logs 的URL模式'''

from django.conf.urls import url

from . import views

urlpatterns = [
    # 主页
    # 调用 views.index,指定其名称为 index, 方便其他调用
    url(r'^$',views.index, name='index'),
    
    # 显示所有的主题
    url(r'^topics/$',views.topics,name='topics'),
    # 特定主题的详细页面
    url(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),
    # 用于添加新主题的网页
    url(r'^new_topic/$',views.new_topic,name='new_topic'),
    ]
