from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    '''注册新用户'''
    if request.method !="POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            # 让用户自动登陆，在重定向到主页，注册时输入了两次密码，返回通过身份验证的对象
            authenticated_user = authenticate(username=new_user.username,
                password=request.POST['password1'])
            login(request,authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    
    context = {'form':form}
    return render(request, 'users/register.html', context)
