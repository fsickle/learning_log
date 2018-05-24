from django.shortcuts import render
from .models import Topic
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import TopicForm


def index(request):
    '''学习笔记主页'''
    return render(request,'learning_logs/index.html')

def topics(request):
    '''显示所有的主题'''
    # 按照属性 date_added 对它们进行排序
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request,'learning_logs/topics.html',context)
    
def topic(request,topic_id):
    # 单个主题与其所有的条目
    topic = Topic.objects.get(id=topic_id) # topic_id 为正则表达式捕获的值
    entries = topic.entry_set.order_by('-date_added') # - 表示降序
    context = {'topic':topic,'entries':entries}
    return render(request,'learning_logs/topic.html',context)
    
def new_topic(request):
    '''添加新主题'''
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form  = TopicForm()
    else:
        # POST提交的数据，对数据处理
        form = TopicForm(request.POST)
        # 判断数据是否有效
        if form.is_valid():
            form.save()
            # 重定向到网页 topics,reverse,根据指定的URL模型确定URL
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form':form}
    return render(request,'learning_logs/new_topic.html',context)

