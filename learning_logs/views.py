from django.shortcuts import render
from .models import Topic,Entry
from django.http import HttpResponseRedirect,Http404
from django.core.urlresolvers import reverse
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required



def index(request):
    '''学习笔记主页'''
    return render(request,'learning_logs/index.html')

@login_required
def topics(request):
    '''显示所有的主题'''
    # 按照属性 date_added 对它们进行排序
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics':topics}
    return render(request,'learning_logs/topics.html',context)

@login_required   
def topic(request,topic_id):
    # 单个主题与其所有的条目
    topic = Topic.objects.get(id=topic_id) # topic_id 为正则表达式捕获的值
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added') # - 表示降序
    context = {'topic':topic,'entries':entries}
    return render(request,'learning_logs/topic.html',context)

@login_required    
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
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            # 重定向到网页 topics,reverse,根据指定的URL模型确定URL
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form':form}
    return render(request,'learning_logs/new_topic.html',context)

@login_required    
def new_entry(request,topic_id):
    '''在特定的主题中添加新条目'''
    topic = Topic.objects.get(id=topic_id)
    
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False) # 不保存在数据库
            new_entry.topic = topic # 把 topic 赋给
            new_entry.save() #保存数据库
            return HttpResponseRedirect(reverse('learning_logs:topic',
                    args=[topic.id]))
                    
    context = {'topic':topic,'form':form}
    return render(request,'learning_logs/new_entry.html',context)
    
@login_required
def edit_entry(request,entry_id):
    '''编辑既有条目'''
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    
    if request.method != 'POST':
        form = EntryForm(instance=entry) # 使用既有条目填充
    
    else:
        form = EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                args=[topic.id]))
    
    context = {'entry':entry,'topic':topic,'form':form}
    return render(request,'learning_logs/edit_entry.html',context)

